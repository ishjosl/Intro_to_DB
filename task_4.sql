-- SQL script to print a basic description of the 'books' table
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'  -- Specify the database name directly
  AND TABLE_NAME = 'Books';
