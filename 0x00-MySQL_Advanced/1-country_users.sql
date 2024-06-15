-- Script that creates a table users following these requirements:
-- Creates a table with unique id-nn,ai,pk; email-str(255) name-str(255)
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null
-- (= default will be the first element of the enumeration, here US)
CREATE Table users if not exist (
    id INT NOT NULL auto increment primary key,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR(225),
    country ENUM("US", "CO", "TN") DEFAULT "US" NOT NULL
);