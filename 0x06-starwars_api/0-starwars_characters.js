#!/usr/bin/node

const request = require('request');

const movID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movID}`;

const req = (arr, i) => {
  if (i === arr.length) return;
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      req(arr, i + 1);
    }
  });
};

request(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(res.body);
    req(chars.characters, 0);
  }
});
