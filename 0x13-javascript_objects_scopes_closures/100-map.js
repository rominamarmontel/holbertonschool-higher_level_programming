#!/usr/bin/node
const list = require('./100-data.js').list;
const newlist = list.map((x, y) => x * y);
console.log(list);
console.log(newlist);
