#!/usr/bin/node

// rename Square to pastSquare to use inheritance without conflict
const pastSquare = require('./5-square.js');

// create class Square inherit from Rectangle
class Square extends pastSquare {
  constructor (size) {
    super(size, size);
  }

  // prints the square using C
  charPrint (c) {
    // charUsed char used to print, if not : default 'X'
    let charUsed = 'X';
    if (c !== undefined) {
      charUsed = c;
    }
    // use this.width or this.height to print
    for (let i = 0; i < this.width; i++) {
      console.log(charUsed.repeat(this.width));
    }
  }
}

// export class to be used on other file
module.exports = Square;
