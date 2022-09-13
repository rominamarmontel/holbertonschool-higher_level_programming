#!/usr/bin/node
//Write a script that gets the contents of a webpage and stores it in a file
const axios = require('axios').default;
const fs = require('fs');

request.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, 'utf8', (error) => {
        if (error) {
          console.log(error);
        }
      });
    });
