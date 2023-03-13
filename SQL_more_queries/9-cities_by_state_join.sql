-- list all cities contained in database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities
JOIN hbtn_0d_usa.states ON states.id = cities.state_id
ORDER BY cities.id;