#!/usr/bin/node

// create empty class
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

// export class to be used on other file
module.exports = Rectangle;
