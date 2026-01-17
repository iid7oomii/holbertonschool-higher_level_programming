-- 9-cities_by_state_join.sql
-- List all cities in the database with their corresponding state name
-- Each record shows: cities.id - cities.name - states.name
-- Results are sorted by cities.id in ascending order
-- Only one SELECT statement is used

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
