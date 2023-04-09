#!/usr/bin/node

// count variable
let callCount = 0;

// export function that print the number of arg already printed
// and new argument value
exports.logMe = function (item) {
  const joined = `${callCount}: ${item}`;
  console.log(joined);
  // increment count of call function logMe
  callCount += 1;
}
;
