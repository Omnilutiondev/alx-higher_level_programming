#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < size; idx++) {
    let row = '';
    for (let mn = 0; mn < size; mn++) row += 'X';
    console.log(row);
  }
}
