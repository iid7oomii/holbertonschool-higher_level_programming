-- lists all records of the table second_table
-- use select and not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
