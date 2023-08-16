-- SQL script that creates database and table with unique
-- auto generated, non null, primary key id column
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
