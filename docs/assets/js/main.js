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
              this.updateUIForRaspberryPiEnvironmentSensors(doc_obj)
              this.updateUIForRaspberryPiAmbilight(doc_obj)
            })
          })
        })
        .catch(err => {

        })
    },
    updateUIForRaspberryPiEnvironmentSensors(doc_obj) {
      const domObj = document.querySelector(`.${doc_obj.id}.environment`)
      if(domObj === null) {
        this._$pis.innerHTML += `
          <div class="grid__column-12 grid__column-md-6 grid__column-lg-4 grid__column-xl-2 card__container">
          <div class="card ${doc_obj.id} environment">
            <header class="card__header">
              <i class="fas fa-thermometer-half environment__bulb"></i>
              <h2 class="card__title">RasPi: ${doc_obj.id} - Environment</h2>
              <span></span>
            </header>
            <section class="card__main">
              <table>
                <tr>
                  <td>Date</td>
                  <td class="environment__modified_at"><span class="value">${convertTimeMillisToDate(doc_obj.data().environment.modifiedAt)}</span><span class="unit"></span></td>
                </tr>   
                <tr>
                  <td>Temperature</td>
                  <td class="temperatiure__value"><span class="value">${doc_obj.data().environment.temperature.value}</span><span class="unit">${ doc_obj.data().environment.temperature.unit_code }</span></td>
                </tr>
                <tr>
                  <td>Humidity</td>
                  <td class="humidity__value"><span class="value">${doc_obj.data().environment.humidity.value}</span><span class="unit">${ doc_obj.data().environment.humidity.unit_code }</span></td>
                </tr>
                <tr>
                  <td>Pressure</td>
                  <td class="pressure__value"><span class="value">${doc_obj.data().environment.pressure.value}</span><span class="unit">${ doc_obj.data().environment.pressure.unit_code }</span></td>
                </tr>
              </table>
            </section>
            <footer class="card__footer">
            </footer>
          </div> 
          </div>
        `
      } else {
        const _$environmentElement = document.querySelector(`.${doc_obj.id}.environment`)
        const _$environment__modified_at = _$environmentElement.querySelector(`.environment__modified_at`)
        if(_$environment__modified_at) {
          _$environment__modified_at.innerHTML = `<span class="value">${convertTimeMillisToDate(doc_obj.data().environment.modifiedAt)}</span><span class="unit"></span>`
        }
        const _$temperatiure__value = _$environmentElement.querySelector(`.temperatiure__value`)
        if(_$temperatiure__value) {
          _$temperatiure__value.innerHTML = `<span class="value">${doc_obj.data().environment.temperature.value}</span><span class="unit">${ doc_obj.data().environment.temperature.unit_code }</span>`
        }
        const _$humidity__value = _$environmentElement.querySelector(`.humidity__value`)
        if(_$humidity__value) {
          _$humidity__value.innerHTML = `<span class="value">${doc_obj.data().environment.humidity.value}</span><span class="unit">${ doc_obj.data().environment.humidity.unit_code }</span>`
        }
        const _$pressure__value = _$environmentElement.querySelector(`.pressure__value`)
        if(_$pressure__value) {
          _$pressure__value.innerHTML = `<span class="value">${doc_obj.data().environment.pressure.value}</span><span class="unit">${ doc_obj.data().environment.pressure.unit_code }</span>`
        }
      }
    },
    updateUIForRaspberryPiAmbilight(doc_obj) {
      const domObj = document.querySelector(`.${doc_obj.id}.ambilight`)
      if(domObj === null) {
        this._$pis.innerHTML += `
          <div class="grid__column-12 grid__column-md-6 grid__column-lg-4 grid__column-xl-2 card__container">
          <div class="card ${doc_obj.id} ambilight">
            <header class="card__header">
              <i class="far fa-lightbulb rgbmatrix__bulb"></i>
              <h2 class="card__title">RasPi: ${doc_obj.id} - Ambilight</h2>
              <span></span>
            </header>
            <section class="card__main">
              <div class="ambilight__color-value" style="background: ${doc_obj.data().ambilight.color.value};">${doc_obj.data().ambilight.color.value}</div>
            </section>
            <footer class="card__footer">
            </footer>
          </div> 
          </div>
        `
      } else {
        const _$ambilightElement = document.querySelector(`.${doc_obj.id}.ambilight`)
        const _$ambilight__color_value = _$ambilightElement.querySelector(`.ambilight__color-value`)
        if(_$ambilight__color_value) {
          _$ambilight__color_value.style.background = doc_obj.data().ambilight.color.value
        }
      }
    },
    cacheDOMElements() {
      // Environment DOM Elements
      this._$pis = document.querySelector('#pis')
    }
  }

  // Initalize application
  app.init()
})(window)