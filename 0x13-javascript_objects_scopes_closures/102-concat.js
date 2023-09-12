#!/usr/bin/node
const { argv } = require('process');
const file = require('fs');

file.readFile(argv[2], (err, data) => {
  if (err) {
    throw err;
  }
  file.appendFile(argv[4], data, (err) => {
    if (err) {
      throw err;
    }
  });
});

file.readFile(argv[3], (err, data) => {
  if (err) {
    throw err;
  }
  file.appendFile(argv[4], data, (err) => {
    if (err) {
      throw err;
    }
  });
});
