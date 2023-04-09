#!/usr/bin/node

// create class Rectangle
class Rectangle {
  constructor (w, h) {
    // assign w and h value only if both are greater than 0
    if (w > 0 && h > 0) this.width = w;
    if (w > 0 && h > 0) this.height = h;
  }
}

// export class to be used on other file
module.exports = Rectangle;
