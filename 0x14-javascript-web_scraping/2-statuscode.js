#!/usr/bin/node
// Script that takes a url and makes a get request
// then prints the status

const args = process.argv;

const request = require('request');

request(args[2], function (error, response, body) {
  console.error('error:', error);
  console.log('code:', response.statusCode);
});
