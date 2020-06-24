#!/usr/bin/node
const filmId = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmId + '/';
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
