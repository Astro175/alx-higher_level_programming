#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

if (process.argv.length !== 4) {
  console.log('Usage: ./add.js <integer1> <integer2>');
} else if (isNaN(parseInt(process.argv[2])) || isNaN(parseInt(process.argv[3]))) {
  console.log('Arguments must be integers');
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  add(a, b);
}
