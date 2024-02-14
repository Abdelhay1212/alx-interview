#!/usr/bin/node
/* Star Wars Characters */
const request = require('request');

const args = process.argv.slice(2);
const id = args[0];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const person of characters) {
      request(person, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const data = JSON.parse(body);
          console.log(data.name);
        } else {
          console.log(error);
        }
      });
    }
  } else {
    console.error(error);
  }
});
