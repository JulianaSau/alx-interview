#!/usr/bin/node
const request = require('request');
const filmURL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${filmURL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const characterName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promisErr, __, charactersReqBody) => {
          if (promisErr) {
            reject(promisErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(characterName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
