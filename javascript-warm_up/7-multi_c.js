#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;
const str = 'C is fun';

// argv[2] is number time repeat script
if (parseInt(args[2])) {
  for (let i = 0; i < args[2]; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
