CREATE TABLE flights(
    id SERIAL PRIMARY KEY, 
    orign VARCHAR NOT NULL, 
    destination VARCHAR NOT NULL,   
    duration INTEGER NOT NULL
);