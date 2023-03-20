-- Lists all the cities in a database
SELECT cities.id, cities.name, states.name
FROM CITIES
INNER JOIN ON cities.state_id=states.id
ORDER BY cities.id ASC;
