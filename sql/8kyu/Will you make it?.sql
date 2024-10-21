-- Write your SQL statement here: you are given a table 'zerofuel' with columns 'distance_to_pump', 'mpg' and 'fuel_left'
-- Return a table with all the columns and your result in a column named 'res'.
SELECT
  distance_to_pump,
  mpg,
  fuel_left,
  CASE
      WHEN distance_to_pump <= mpg * fuel_left THEN True
      ELSE False
  END AS res
FROM
    zerofuel;