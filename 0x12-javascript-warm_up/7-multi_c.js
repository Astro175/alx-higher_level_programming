#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length !== 1) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(arg[0]);
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
