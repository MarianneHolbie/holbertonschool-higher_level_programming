#!/usr/bin/node

// export function return number of occurence in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count += 1;
    }
  }
  return (count);
};
