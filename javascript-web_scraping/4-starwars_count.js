#!/usr/bin/node

// Include module
const process = require('process');
const request = require('request');

// use process to store argv in command line
const args = process.argv;
// request API
const URL = args[2];

// stock all films
request.get(URL, (err, response, body) => {
  if (err) {
    console.error('error', err);
  } else {
    // films = all films in the given Starwars API
    const films = JSON.parse(body).results;

    // initialize count
    let counter = 0;

    // read all films properties
    for (const episode of films) {
      // search if character Wedge Antilles id='18'
      for (const people of episode.characters) {
        if (people.includes('18')) {
          counter++;
        }
      }
    }

    console.log(counter);
  }
});
