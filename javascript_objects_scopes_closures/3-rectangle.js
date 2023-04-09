#!/usr/bin/node

// create class Rectangle
class Rectangle {
  constructor (w, h) {
    // assign w and h value only if both are greater than 0
    if (w > 0 && h > 0) this.width = w;
    if (w > 0 && h > 0) this.height = h;
  }

  // prints the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

// export class to be used on other file
module.exports = Rectangle;
