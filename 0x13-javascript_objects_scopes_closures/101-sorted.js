#!/usr/bin/node
const dict = require('./101-data').dict;

const ttlist = Object.entries(dict);
const vaals = Object.values(dict);
const valUniq = [...new Set(vaals)];
const newDict = {};
for (const q in valUniq) {
  const list = [];
  for (const w in ttlist) {
    if (ttlist[w][1] === valUniq[q]) {
      list.unshift(ttlist[w][0]);
    }
  }
  newDict[valUniq[q]] = list;
}
console.log(newDict);
