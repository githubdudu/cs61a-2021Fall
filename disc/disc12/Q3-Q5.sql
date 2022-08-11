-- Q3
-- Write a query that outputs the names of employees that Oliver Warbucks directly supervises.
SELECT name FROM records WHERE supervisor = 'Oliver Warbucks';

-- Q4
-- Write a query that outputs all information about employees that supervise themselves.
SELECT * FROM records WHERE supervisor = name;

-- Q5
-- Write a query that outputs the names of all employees with salary greater than 50,000 in alphabetical order.
SELECT name  FROM records WHERE salary > 50000 ORDER BY name asc;