#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

// argv[2] is size of square
if (parseInt(args[2])) {
  for (let i = 0; i < args[2]; i++) {
    console.log('X'.repeat(args[2]));
  }
} else {
  console.log('Missing size');
}
