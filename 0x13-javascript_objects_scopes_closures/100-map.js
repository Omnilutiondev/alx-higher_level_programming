#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (nmb, idx) {
  return nmb * idx;
});

console.log(list);
console.log(newList);
