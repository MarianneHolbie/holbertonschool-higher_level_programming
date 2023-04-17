#!/usr/bin/node

// Include module
const process = require('process');
const request = require('request');

// use process to store argv in command line
const args = process.argv;

// print status code of GET request
request.get(args[2], (err, response) => {
  // print the error if occured
  if (err) {
    console.error('error', err);
  } else {
  // print "code: <status code>"
    console.log('code:', response.statusCode);
  }
});
