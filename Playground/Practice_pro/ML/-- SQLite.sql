-- SQLite
SELECT name, total_population, per_capita_income FROM states
WHERE median_age > 35 AND total_households > 50000
GROUP BY name
ORDER BY total_population DESC;
