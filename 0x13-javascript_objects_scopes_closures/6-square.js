#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
