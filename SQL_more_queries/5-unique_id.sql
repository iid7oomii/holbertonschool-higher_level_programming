-- creates the table unique_id with description and default id value 1 and must be unique
-- use default and unique
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE ,
name VARCHAR(256)
);
