#!/usr/bin/node

// Include process module
const process = require('process');

// use process to store argv in command line
const args = process.argv;

// file system (fs) module
const requestfile = require('fs');

// readfile
requestfile.readFile(args[2], 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content.toString());
  }
});
