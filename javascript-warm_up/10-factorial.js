#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

// args[2] is integer to factorial
const number = parseInt(args[2]);

// function factorial number
function factorial (n) {
  // if n = 0, return 1
  if (n === 0 || isNaN(n)) {
    return (1);
  } else {
  // call recursiv factorial
    return n * factorial(n - 1);
  }
}

console.log(factorial(number));
