#!/usr/bin/node

const argv1 = process.argv[2];

const num = parseInt(argv1);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
