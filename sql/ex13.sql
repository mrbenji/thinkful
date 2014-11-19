ALTER TABLE person ADD COLUMN dead INTEGER;
ALTER TABLE person ADD COLUMN phone_number TEXT;
ALTER TABLE person ADD COLUMN salary FLOAT;
ALTER TABLE person ADD COLUMN dob DATETIME;
ALTER TABLE person_pet ADD COLUMN purchased_on DATETIME;
ALTER TABLE pet ADD COLUMN parent INTEGER;

UPDATE person SET dead = 0;

UPDATE person SET 
    phone_number = "408-555-0563", 
    salary = 100000.99, 
    dob = "1973-11-21" 
WHERE first_name = "Benji" AND last_name = "Tittle";

UPDATE person SET 
    phone_number = "408-555-9909", 
    salary = 75000.99, 
    dob = "1976-09-03" 
WHERE first_name = "Danielle" AND last_name = "Tittle";

UPDATE person SET 
    phone_number = "310-555-9050", 
    salary = 200000.99, 
    dob = "1976-09-21" 
WHERE first_name = "David" AND last_name = "Tittle";

-- SELECT * FROM person;

-- Yeah, we bought all our pets on the same day in the future, 
-- so sue me... we happen to own a time machine timeshare. 
UPDATE person_pet SET purchased_on = "2015-10-21";

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
    SELECT 3, "Kathryn", "Tittle", 8, 0, "408-849-4100", 156.00, "2006-08-18"
    UNION ALL
    SELECT 4, "Samuel", "Tittle", 6, 0, "408-849-4100", 156.00, "2008-11-01"
    UNION ALL
    SELECT 5, "Ivy", "Tittle", 12, 1, "310-555-9050", 0.00, "2002-07-02";

INSERT INTO pet (id, name, breed, age, dead, dob, parent)
    SELECT 4, "Lucky", "Bear", 1, 0, "2014-06-12", (SELECT id FROM pet WHERE name = "Wilson")
    UNION ALL
    SELECT 5, "Fluffy", "Bear", 0, 0, "2014-09-15", (SELECT id FROM pet WHERE name = "Wilson");
