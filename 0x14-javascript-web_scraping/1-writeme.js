#!/usr/bin/node
//Write a script that writes a string to a file
const fs = require('fs');
//fs.open(新規作成ファイルのパス, 書き込む文字, コールバック関数)
fs.writeFile(process.argv[2], process.argv[3], (err) => {
    if(err) {
        console.log(err);
    }
});
