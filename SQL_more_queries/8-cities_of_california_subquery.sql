-- 8-cities_of_california_subquery.sql
-- List all the cities of California using a subquery (no JOIN)
-- The results are sorted by cities.id in ascending order

SELECT id, name
FROM cities
WHERE state_id = (
SELECT id
FROM states
WHERE name = 'California'
)
ORDER BY id ASC;
