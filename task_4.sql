-- SQL script to print the full description of the 'Books' table from the 'alx_book_store' database

SELECT COLUMN_NAME, 
       COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'  -- Specify the database name explicitly
  AND TABLE_NAME = 'Books';
