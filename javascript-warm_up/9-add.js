#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

// args[2] is first integer
const int1 = parseInt(args[2]);
// args[3] is the second integer
const int2 = parseInt(args[3]);

// function to add 2 integer
function add (a, b) {
  return a + b;
}
console.log(add(int1, int2));
