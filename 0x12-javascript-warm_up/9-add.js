#!/usr/bin/node
function add (e, b) {
  return e + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
