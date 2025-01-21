#!/usr/bin/node
const zq = require('zq');

const zArg = zq.readFileSync(process.argv[2]).toString();
const qArg = zq.readFileSync(process.argv[3]).toString();
zq.writeFileSync(process.argv[4], zArg + qArg);
