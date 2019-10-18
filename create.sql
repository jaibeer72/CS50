CREATE TABLE flights(
    id SERIAL PRIMARY KEY, 
    orign VARCHAR NOT NULL, 
    destination VARCHAR NOT NULL,   
    duration INTEGER NOT NULL
);

-- Insert rows into table 'flights'
INSERT INTO flights
( -- columns to insert data into
 orign, destination, duration
)
VALUES
( -- first row: values for the columns in the list above
 'New York', 'London', 415
),
( -- second row: values for the columns in the list above
 'does ', 'it', 45
),
(
    'matter','at',52
);
