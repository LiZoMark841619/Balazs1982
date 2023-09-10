-- SQLite
SELECT * FROM astronauts;

SELECT Status, COUNT(*) AS Total, 
ROUND(AVG(Space_Flight_hr)) AS Avg_time_in_space_hr
FROM astronauts
GROUP BY status
ORDER BY Avg_time_in_space_hr;

SELECT Gender, ROUND(AVG(Space_Flight_hr)) AS Avg_time_in_space_hr
FROM astronauts
GROUP BY Gender;

SELECT Name, Space_Flight_hr AS Time_in_space_hr
FROM astronauts
GROUP BY Name
ORDER BY Time_in_space_hr DESC
LIMIT 5;

SELECT Name, Space_Flight_hr,
    CASE
        WHEN Space_Flight_hr < 1000 THEN "junior"
        WHEN Space_Flight_hr < 4000 THEN "medior"
        WHEN Space_Flight_hr < 8000 THEN "senior"
        WHEN Space_Flight_hr > 8000 THEN "king"
        ELSE "other_level"
    END as "Levels"
FROM astronauts;

SELECT COUNT(*) AS Total,
    CASE
        WHEN Space_Flight_hr < 1000 THEN "junior"
        WHEN Space_Flight_hr < 4000 THEN "medior"
        WHEN Space_Flight_hr < 8000 THEN "senior"
        WHEN Space_Flight_hr > 8000 THEN "king"
        ELSE "other_level"
    END as "Levels"
FROM astronauts
GROUP BY Levels;

SELECT Name, Gender, Space_Walks, Space_Walks_hr AS Space_walks_hr
FROM astronauts
GROUP BY Name
HAVING Space_Walks > 5
ORDER BY Space_walks_hr DESC
LIMIT 5;


