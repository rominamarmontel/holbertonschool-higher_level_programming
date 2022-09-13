#!/usr/bin/node
//Write a script that prints the title of a Star Wars movie 
//where the episode number matches a given integer
const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error);
  });