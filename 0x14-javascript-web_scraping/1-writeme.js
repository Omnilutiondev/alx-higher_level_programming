#!/usr/bin/node
const frg = require('frg');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
