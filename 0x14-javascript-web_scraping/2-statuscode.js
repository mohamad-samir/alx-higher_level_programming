#!/usr/bin/node

const request = require('request');

// Check if the file path argument and string to write is provided
if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <URL>');
  process.exit(1);
}

// Get the URL from command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.error('Error making request:', error);
    process.exit(1);
  }

  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
