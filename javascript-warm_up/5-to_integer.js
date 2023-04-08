#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

// if args[2] is not a Number return NaN
// use parseInt to transform as int (also trunc float)
if (isNaN(Number(args[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(args[2]));
}
