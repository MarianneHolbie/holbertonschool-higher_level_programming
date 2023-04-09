#!/usr/bin/node

// export function return reversed version of list
exports.esrever = function (list) {
  // return list
  const tsil = [];
  // calculate the index of last element of list
  let i = list.length - 1;
  // add each element of list (start end) to reversed list
  for (i; i >= 0; i--) {
    tsil.push(list[i]);
  }
  return (tsil);
};
