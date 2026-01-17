-- creates the table id_not_null with description and id INT with the default value 1
-- use default
CREATE TABLE IF NOT EXISTS id_not_null (
id INT NOT NULL DEFAULT 1 ,
name VARCHAR (256)
);
