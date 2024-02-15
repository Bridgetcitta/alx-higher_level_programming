-- Script that displays the average temperature in (Fahrenheit) by city. 
-- ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS `ave_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `ave_temp` DESC;
