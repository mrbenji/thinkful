DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS pet;
DROP TABLE IF EXISTS species;
DROP TABLE IF EXISTS breed;
DROP TABLE IF EXISTS person_pet;

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);

INSERT INTO person (id, first_name, last_name, age)
    SELECT 0, "Benji", "Tittle", 40
    UNION ALL
    SELECT 1, "Danielle", "Tittle", 37
    UNION ALL
    SELECT 2, "David", "Tittle", 37;

CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER,
    dob DATETIME
);

INSERT INTO pet (id, name, breed, age, dead, dob)
    SELECT 0, "Wilson", "Domestic Shorthair", 5, 0, "2009-11-01"
    UNION ALL
    SELECT 1, "Mowgli", "Tonkinese", 4, 1, "2000-10-15"
    UNION ALL
    SELECT 2, "Hollie", "German Shepherd", 8, 0, "2006-06-10"
    UNION ALL
    SELECT 3, "Einstein", "Poodle", 2, 1, "2010-11-05";

CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
);

INSERT INTO person_pet (person_id, pet_id)
    SELECT  0, 0
    UNION ALL
    SELECT  0, 1
    UNION ALL
    SELECT  1, 0
    UNION ALL
    SELECT  1, 1
    UNION ALL
    SELECT  2, 2
    UNION ALL
    SELECT  2, 3;
