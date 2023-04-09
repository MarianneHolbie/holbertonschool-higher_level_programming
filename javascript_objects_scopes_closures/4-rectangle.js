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

  // exhange height and width
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  // multiplies by 2 height and width
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

// export class to be used on other file
module.exports = Rectangle;
