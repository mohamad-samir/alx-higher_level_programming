#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Check if the file path argument and the URL are provided
if (process.argv.length < 4) {
  console.error('Usage: node <script-file> <URL> <output-file>');
  process.exit(1);
}

// Get the file path and URL from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the API endpoint
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    process.exit(1);
  }

  // Write to the file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
