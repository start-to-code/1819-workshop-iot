'use strict';
// Imports
const sense = require('sense-hat-led');

// Constants
const X = [0, 255, 255];
const O = [0, 0, 0];
const COLOR = [255, 0, 0];

// Function: randomColor()
function randomColor() {
    return [
        Math.round(Math.random()*255),
        Math.round(Math.random()*255),
        Math.round(Math.random()*255)
    ]
}

// Function: lashLED(x, y, delay)
function flashLED(x, y, delay) {
    setTimeout(() => {
        sense.setPixel(x, y, randomColor());
        flashLED(x, y, delay)
    }, delay);
}

sense.clear();
for(let x=0;x<=7;x+=2) {
    for(let y=0;y<=7;y+=2) {
        flashLED(x, y, 400+Math.round(Math.random()*2600));
    }
}