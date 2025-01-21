#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let v = 0; v < list.length; v++) {
    if (searchElement === list[v]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
