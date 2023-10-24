#!/usr/bin/node

const fs = require('fs');

// Check if the file path argument and string to write is provided
if (process.argv.length < 4) {
  console.error('Usage: node <script-file> <file-path> <string-to-write>');
  process.exit(1);
}

// Get the file path and string from command line arguments
const filePath = process.argv[2];
const string = process.argv[3];

// Read the file in UTF-8 encoding
fs.writeFile(filePath, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
