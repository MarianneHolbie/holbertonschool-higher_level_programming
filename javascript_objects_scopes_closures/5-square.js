#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// create class Square inherit from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

// export class to be used on other file
module.exports = Square;
