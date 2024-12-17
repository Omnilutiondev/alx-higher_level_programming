#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < x; idx++) {
    console.log('C is fun');
  }
}
