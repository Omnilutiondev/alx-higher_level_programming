#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (l) {
    if (l === undefined) {
      l = 'X';
    }
    for (let v = 0; v < this.height; v++) {
      let t = '';
      for (let k = 0; k < this.width; k++) {
        t += l;
      }
      console.log(t);
    }
  }
}

module.exports = Square;
