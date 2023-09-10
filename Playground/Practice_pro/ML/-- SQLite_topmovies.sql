-- SQLite
-- What are average, max, and min values in the data?
-- What about those numbers per category in the data (using HAVING)?
-- What ways are there to group the data values that don’t exist yet (using CASE)?
-- What interesting ways are there to filter the data (using AND/OR)?
SELECT * FROM topmovies;

SELECT Title, Worldwide, AVG(Worldwide) AS average, MIN(Worldwide) AS minimum,
FROM topmovies
GROUP BY Title
HAVING Worldwide > minimum AND Worldwide < average;