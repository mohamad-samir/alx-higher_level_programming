-- SQL query to list all cities contained in the database
-- in a speficed format, using joins
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
