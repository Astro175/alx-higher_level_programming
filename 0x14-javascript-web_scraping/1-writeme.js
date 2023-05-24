#!/usr/bin/node
// Script that writes into a file

const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
