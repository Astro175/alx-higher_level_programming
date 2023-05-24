#!/usr/bin/node
// Script that prints star wars movie title
// if id argument is passed

const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (error, reponse, body) => {
  if (error) console.log(error);
  const movie = JSON.parse(body);
  console.log(movie.title);
});
