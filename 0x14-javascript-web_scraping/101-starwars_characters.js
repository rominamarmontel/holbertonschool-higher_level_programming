#!/usr/bin/node
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(async function (response) {
    for (let i = 0; i < response.data.characters.length; i++) {
      await axios.get(response.data.characters[i])
        .then(function (response) {
          console.log(response.data.name);
        });
    }
  })
  .catch(function (error) {
    console.log(error);
  });
