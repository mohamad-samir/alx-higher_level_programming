-- SQL script that creates a table force_name
-- on the server with a field that can't be null
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
