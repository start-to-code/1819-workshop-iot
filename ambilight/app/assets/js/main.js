const config = {
  firebase: {
    apiKey: 'AIzaSyAb_oy301KscmyVEypq_3zvmZT-jABqG6I',
    authDomain: 'start-to-code.firebaseapp.com',
    databaseURL: 'https://start-to-code.firebaseio.com',
    projectId: 'start-to-code',
    storageBucket: 'start-to-code.appspot.com',
    messagingSenderId: '659804621253',
  },
  ambilights_collection_name: 'ambilights',
  light_id: 'stc_light_1',
}

;((window) => {
  const app = {
    init() {
      // Initialize firebase
      firebase.initializeApp(config.firebase)
      // Initialize Cloud Firestore through Firebase
      this._firestore = firebase.firestore()
      // Disable deprecated features
      this._firestore.settings({
        timestampsInSnapshots: true
      })
      // Cache DOM-elements
      this.cacheDOMElements(); 

      // Get the ambilight via Firebase collection and document child
      this._ambiLightRef = this._firestore.collection(config.ambilights_collection_name).doc(config.light_id);
      this._ambiLigtData = {
        isOn: false,
        color: {
          value: '#000000',
          type: 'hex'
        }
      }
      this._ambiLightRef.get().then((doc) => {
          if (doc.exists) {
            this._ambiLigtData = doc.data()
            this._ambiLightRef.onSnapshot((doc) => {
              this._ambiLigtData = doc.data()
              this.updateUI();
            })
          }
      }).catch((error) => {
          console.log("Error getting document:", error)
      })
    },
    cacheDOMElements() {
      this._$rgbmatrix = document.querySelector('#rgbmatrix')
      this._$rgbmatrixBulb = document.querySelector('.rgbmatrix__bulb')
      this._$chkRgbmatrixState = document.querySelector('#chkRgbmatrixState')
      if(this._$chkRgbmatrixState) {
        this._$chkRgbmatrixState.addEventListener('change', (ev) => {
          ev.preventDefault()
          this._ambiLigtData.isOn = ev.target.checked
          this.updateAmbilightInFirebase()
          return false
        })
      }
      this._$txtRgbmatrixColor = document.querySelector('#txtRgbmatrixColor')
      if(this._$txtRgbmatrixColor) {
        this._$txtRgbmatrixColor.addEventListener('keyup', (ev) => {
          ev.preventDefault()
          if (ev.key === "Enter") {
            this._ambiLigtData.color.value = ev.target.value
            this._ambiLigtData.color.type = 'hex'

            this.updateUI()
            this.updateAmbilightInFirebase()
          }
          return false
        })
      }
    },
    updateUI() {
      if(this._$rgbmatrix) {
        this._$rgbmatrix.style.background = this._ambiLigtData.color.value
      }
      if(this._$rgbmatrixBulb) {
        this._$rgbmatrixBulb.style.color = this._ambiLigtData.color.value
      }
      if(this._$txtRgbmatrixColor) {
        this._$txtRgbmatrixColor.value = this._ambiLigtData.color.value;
      }
      if(this._$chkRgbmatrixState) {
        this._$chkRgbmatrixState.checked = this._ambiLigtData.isOn;
      }
    },
    updateAmbilightInFirebase() {
      this._ambiLightRef.get().then((doc) => {
          if (doc.exists) {
              this._ambiLightRef.set(this._ambiLigtData, { merge: true }).then(() => {
                console.log('Document updated!')
              }).catch((error) => {
                console.log('Error writing document: ${error}')
              })
          } else {
              console.log("No such document!")
          }
      }).catch((error) => {
          console.log("Error getting document:", error)
      })
    }
  }

  // Initalize application
  app.init()
})(window)