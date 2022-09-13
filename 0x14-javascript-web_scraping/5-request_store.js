#!/usr/bin/node
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
