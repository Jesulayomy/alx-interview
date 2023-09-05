#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;

  for (const person of characters) {
    request.get(person, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
