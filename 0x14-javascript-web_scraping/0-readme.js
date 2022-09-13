#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
fs.readFile(path, 'utf8', (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});