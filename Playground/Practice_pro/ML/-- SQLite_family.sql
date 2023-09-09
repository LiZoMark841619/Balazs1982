-- SQLite
SELECT * FROM family;

SELECT name, num_of_child FROM family WHERE num_of_child !=0;

SELECT name, SUM(age) AS age
FROM family 
GROUP BY name 
HAVING age > 20;