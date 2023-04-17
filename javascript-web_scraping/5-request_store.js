#!/usr/bin/node

// Include module
const process = require('process');
const request = require('request');
const fs = require('fs');

// use process to store argv in command line
const args = process.argv;
// request API and name of file where stock
const URL = args[2];
const filename = args[3];

// stock content of webpage
request.get(URL, (err, response, body) => {
  if (err) {
    console.error('error', err);
  } else {
    // write content in a file
    fs.writeFile(filename, body, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
