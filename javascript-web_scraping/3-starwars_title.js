#!/usr/bin/node

// Include module
const process = require('process');
const request = require('request');

// use process to store argv in command line
const args = process.argv;
// construct request url by adding id film
const URL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

// print title of a Star Wars movie where episode number
request.get(URL, (err, response, body) => {
  if (err) {
    console.error('error', err);
  } else {
    // print title of given episode number
    console.log(JSON.parse(body).title);
  }
});
