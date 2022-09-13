#!/usr/bin/node
//Write a script that prints the number of movies 
//where the character “Wedge Antilles” is present
const axios = require('axios').default;
request.get(process.argv[2])
  .then(function (response) {
    response.data.results.forEach(element => {
        for (let i = 0; i < element.characters.length; i++) {
          if (element.characters[i].includes('people/18/')) { count++; }
        }
      });
    })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    console.log(count);
});
