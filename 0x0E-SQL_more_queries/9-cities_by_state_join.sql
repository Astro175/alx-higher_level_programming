-- Lists all the cities in a database
SELECT cities.id, cities.name, states.name
FROM CITIES
INNER JOIN ON cities.states_id=states.id
ORDER BY cities.id;
