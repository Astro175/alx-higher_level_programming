#!/usr/bin/node
// Script that reads and writes into a file

const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString());
});
