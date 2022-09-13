#!/usr/bin/node
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    const dico = {};
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed === true) {
        if (!(response.data[i].userId in dico)) {
          dico[response.data[i].userId] = 1;
        } else {
          dico[response.data[i].userId] += 1;
        }
      }
    }
    console.log(dico);
  })
  .catch(function (error) {
    console.log(error);
  });
