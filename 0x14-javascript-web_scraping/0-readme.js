#!/usr/bin/node
//Write a script that reads and prints the content of a file
const fs = require('fs');
//fs.readFileSync(ファイルのパス, 文字コード, コールバック関数)
fs.readFile(process.argv[2], 'utf8', function (error, data) {
    if(data) {//dataがファイルの中身、errは読み込み時のエラー
        console.log(data);
    } else {
        console.log(err);
    }//console.log(error || data);の一行でも良い
});
