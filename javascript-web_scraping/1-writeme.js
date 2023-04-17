#!/usr/bin/node

// Include process module
const process = require('process');

// use process to store argv in command line
const args = process.argv;

// file system (fs) module
const fs = require('fs');

// write in file given name and content
fs.writeFile(args[2], args[3], 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
