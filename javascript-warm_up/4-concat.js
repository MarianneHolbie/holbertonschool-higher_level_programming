#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

// Print argv[2] is argv[3]
console.log('%s is %s', args[2], args[3]);
