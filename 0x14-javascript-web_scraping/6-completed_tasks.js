#!/usr/bin/node

const request = require('request');

// Define the API URL
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    process.exit(1);
  }

  try {
    // Parse the JSON response
    const todos = JSON.parse(body);

    // Create an object to store the counts of completed tasks by user ID
    const completedTasksByUser = {};

    // Filter and count completed tasks
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    // Print the number of completed tasks by each user
    console.log(completedTasksByUser);
    // console.log(JSON.stringify(completedTasksByUser, null, 2));
  } catch (parseError) {
    console.error('Error parsing JSON response:', parseError);
    process.exit(1);
  }
});
