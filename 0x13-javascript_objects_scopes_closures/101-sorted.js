#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.values(dict).reduce((acc, value) => {
  acc[value] = Object.entries(dict)
    .filter(([, v]) => v === value)
    .map(([z]) => z);
  return acc;
}, {});

console.log(newDict);
