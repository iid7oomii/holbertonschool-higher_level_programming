-- lists the number of records with the same score in the table second_table
-- use select count and as number
SELECT COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
