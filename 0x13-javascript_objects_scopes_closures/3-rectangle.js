#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      let t = '';
      for (let l = 0; l < this.width; l++) {
        t += 'X';
      }
      console.log(t);
    }
  }
}

module.exports = Rectangle;

