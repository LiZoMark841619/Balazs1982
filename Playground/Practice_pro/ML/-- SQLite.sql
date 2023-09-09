-- SQLite
SELECT name, total_population, per_capita_income FROM states
WHERE median_age > 35 AND total_households > 50000
GROUP BY name
ORDER BY total_population DESC;

SELECT name, total_population AS total_pop,
white, black, hispanic, asian, american_indian AS indian,
pacific_islander AS pacific, other_race AS other,
median_age, total_households,
owner_occupied_homes_median_value AS homes_median_value	, per_capita_income
FROM states;



