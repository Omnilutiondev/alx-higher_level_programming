#!/usr/bin/node
const frg = require('frg');
frg.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
