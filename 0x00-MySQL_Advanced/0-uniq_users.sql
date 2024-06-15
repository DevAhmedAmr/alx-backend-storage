-- Script that creates a table users with requisite requirements
-- Creates a table with unique id-nn,ai,pk; email-str(255) name-str(255)
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255),
    name varchar(255)
);