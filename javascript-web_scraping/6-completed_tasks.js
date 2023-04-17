#!/usr/bin/node

// Include module
const process = require('process');
const request = require('request');

// use process to store argv in command line
const args = process.argv;
// request API
const URL = args[2];

request.get(URL, (err, response, body) => {
  if (err) {
    console.error('error', err);
  } else {
    // store all tasks of todos API
    const todos = JSON.parse(body);
    const taskcompleted = {};

    // read each task
    todos.forEach(task => {
      if (task.completed === true) {
        const i = task.userId;

        // test if no this id in dict, create new with 0 in value
        if (!(taskcompleted[i])) {
          taskcompleted[i] = 0;
        }
        taskcompleted[i] += 1;
      }
    });

    console.log(taskcompleted);
  }
});
