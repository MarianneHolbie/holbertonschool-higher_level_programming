#!/usr/bin/node

// Include module
const process = require('process');
const request = require('request');

// use process to store argv in command line
const args = process.argv;
// construct request url by adding id film
const URL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

// print all characters of one episode
request.get(URL, (err, response, body) => {
  if (err) {
    console.error('error', err);
  } else {
    // stock all url of characters
    const char = JSON.parse(body).characters;

    for (const people of char) {
    // get the name of each characters by get with url
      request.get(people, (err, response, body) => {
        if (err) {
          console.error('error', err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
