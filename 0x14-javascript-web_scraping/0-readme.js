#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (error, data) => {
    if(data) {
        console.log(data);
    } else {
        console.log(err);
    }
});
