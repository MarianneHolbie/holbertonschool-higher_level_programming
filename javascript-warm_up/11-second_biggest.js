#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

// if no args or only one args print 0
// if many args, return second biggest integer
if (args.length > 3) {
// construct array with only number args
  const arrayNum = args.slice(2);

  // sort array in asc order
  arrayNum.sort(function (a, b) { return a - b; });
  console.log(arrayNum[arrayNum.length - 2]);
} else {
  console.log(0);
}
