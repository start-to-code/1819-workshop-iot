/*
Start 2 Code
============
Workshop: Internet of Things
Application: Raspberry PI dashboard
Description: 
  - Get all the Ambilights and environment sensors from all the Raspberry PI's
Technology:
  - HTML
  - CSS
    - Libraries:
      - fontawesome
  - JavaScript
    - Libraries:
      - firebasejs
Cloud:
  - Firestore (Firebase)
*/

'use strict'

const config = {
  firebase: {
    apiKey: 'AIzaSyAb_oy301KscmyVEypq_3zvmZT-jABqG6I',
    authDomain: 'start-to-code.firebaseapp.com',
    databaseURL: 'https://start-to-code.firebaseio.com',
    projectId: 'start-to-code',
    storageBucket: 'start-to-code.appspot.com',
    messagingSenderId: '659804621253',
  },
  pis_collection_name: 'pis',
}

function convertTimeMillisToDate(millis) {
  const localOffsetDate = new Date().getTimezoneOffset()
  let realLocalDate = new Date(millis)
  realLocalDate.setHours(realLocalDate.getHours()-localOffsetDate/60)
  return realLocalDate.toLocaleString();
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
      this.cacheDOMElements()

      // Get the collection of Raspberry Pi
      this._pisCollection = this._firestore.collection(config.pis_collection_name).get()
        .then(query => {
          query.forEach(doc => {
            doc.ref.onSnapshot((doc_obj) => {
              const domObj = document.querySelector(`#${doc_obj.id}`)
              if(domObj === null) {
                this._$pis.innerHTML += `
                  <div id="${doc_obj.id}">
                    <div class="ambilight">

                    </div> 
                    <div class="environment">
                      <table>
                        <tr>
                          <td>Temperature</td>
                          <td>${doc_obj.data().environment.temperature.value}</td>
                        </tr>
                        <tr>
                          <td>Humidity</td>
                          <td>${doc_obj.data().environment.humidity.value}</td>
                        </tr>
                        <tr>
                          <td>Pressure</td>
                          <td>${doc_obj.data().environment.pressure.value}</td>
                        </tr>
                      </table>
                    </div> 
                  </div>
                `;
              }
            })
          })
        })
        .catch(err => {

        })
      /*this._ambiLightData = {
        isOn: false,
        color: {
          value: '#000000',
          type: 'hex'
        }
      }
      this._environmentData = {
      }
      this._piRef.get().then((doc) => {
          if (doc.exists) {
            console.log(doc.data().ambilight)
            console.log(doc.data().environment)
            this._ambiLightData = doc.data().ambilight
            this._environmentData = doc.data().environment
            this._piRef.onSnapshot((doc) => {
              this._ambiLightData = doc.data().ambilight
              this._environmentData = doc.data().environment
              this.updateUI();
            })
          }
      }).catch((error) => {
          console.log("Error getting document:", error)
      })*/
    },
    creatUI() {

    },
    updateRaspberryPi(pi_id) {

    },
    cacheDOMElements() {
      // Environment DOM Elements
      this._$pis = document.querySelector('#pis')
    },
    updateUI() {
      if(this._$rgbmatrix) {
        this._$rgbmatrix.style.background = this._ambiLightData.color.value
      }
      if(this._$rgbmatrixBulb) {
        this._$rgbmatrixBulb.style.color = this._ambiLightData.color.value
      }
      if(this._$txtRgbmatrixColor) {
        this._$txtRgbmatrixColor.value = this._ambiLightData.color.value;
      }
      if(this._$chkRgbmatrixState) {
        this._$chkRgbmatrixState.checked = this._ambiLightData.isOn;
      }

      // Environment
      if(this._$environment__modified_at) {
        this._$environment__modified_at.innerHTML = `<span class="value">${ convertTimeMillisToDate(this._environmentData.modifiedAt) }</span>`
      }
      if(this._$environment__temperature) {
        this._$environment__temperature.innerHTML = `<span class="value">${this._environmentData.temperature.value}</span><span class="label">${this._environmentData.temperature.unit_code} (${this._environmentData.temperature.unit_text})</span>`
      }
      if(this._$environment__humidity) {
        this._$environment__humidity.innerHTML = `<span class="value">${this._environmentData.humidity.value}</span><span class="label">${this._environmentData.humidity.unit_code} (${this._environmentData.humidity.unit_text})</span>`
      }
      if(this._$environment__pressure) {
        this._$environment__pressure.innerHTML = `<span class="value">${this._environmentData.pressure.value}</span><span class="label">${this._environmentData.pressure.unit_code} (${this._environmentData.pressure.unit_text})</span>`
      }
    },
    updateAmbilightInFirebase() {
      this._piRef.get().then((doc) => {
          if (doc.exists) {
              this._piRef.set({ ambilight: this._ambiLightData }, { merge: true }).then(() => {
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