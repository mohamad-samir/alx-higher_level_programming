#!/usr/bin/node

const request = require('request');

// Check if the APU URL is provided
if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <URL>');
  process.exit(1);
}

// Get the ID from command line arguments
const apiUrl = process.argv[2];
// const apiUrl = `https://swapi-api.alx-tools.com/api/films/`;

// Make a GET request to the API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    process.exit(1);
  }

  // Parse the JSON string to object
  try {
    let count = 0;
    const charId = 18;
    const movies = JSON.parse(body);
    for (const movie of movies.results) {
      for (const character of movie.characters) {
        if (character.includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  } catch (error) {
    console.error('Error parsing body:', error);
    process.exit(1);
  }
});
