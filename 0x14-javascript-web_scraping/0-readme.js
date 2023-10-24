#!/usr/bin/node

const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error('Usage: node read-file.js <file-path>');
  process.exit(1);
}

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file in UTF-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
