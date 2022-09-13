#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    let count = 0;
    const list = response.data.results;
    for (let i = 0; i < list.length; i++) {
      for (let x = 0; x < list[i].character.length; x++) {
        if (list[i].character[x].includes('/18/') === true) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  });
