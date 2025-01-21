#!/usr/bin/node
const fs = require('fs');

try {
  const fileContent1 = fs.readFileSync(process.argv[2], 'utf8');
  const fileContent2 = fs.readFileSync(process.argv[3], 'utf8');
  fs.writeFileSync(process.argv[4], fileContent1 + fileContent2);
} catch (error) {
  console.error(error);
}
