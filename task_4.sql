-- SQL script to print the full description of the 'books' table from the provided database

SELECT COLUMN_NAME, 
       DATA_TYPE, 
       IS_NULLABLE, 
       COLUMN_DEFAULT, 
       CHARACTER_MAXIMUM_LENGTH, 
       NUMERIC_PRECISION, 
       NUMERIC_SCALE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = DATABASE()  -- The database name is passed as an argument to the mysql command
  AND TABLE_NAME = 'books';
