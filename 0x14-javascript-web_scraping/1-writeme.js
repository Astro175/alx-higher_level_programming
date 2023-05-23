#!/usr/bin/node
// Script that writes into a file

const fs = require('fs');
const args = process.argv;
const newline = '\n';

fs.writeFile(args[2], args[3] + newline, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
