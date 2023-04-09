#!/usr/bin/node

// export function to convert number from base 10 to another given base
exports.converter = function (base) {
  // function that takes the number to convert
  return function (number) {
    // toString convert number base-10 integer in given base base
    return (number.toString(base));
  };
};
