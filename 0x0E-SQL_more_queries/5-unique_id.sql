-- SQL script that creates table on the server,
-- having a column with a default value containing unique values
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
