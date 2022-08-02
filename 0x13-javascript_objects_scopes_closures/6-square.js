#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c === 'C') {
        console.log('C'.repeat(this.size));
      } else {
        console.log('X'.repeat(this.size));
      }
    }
  }
};
