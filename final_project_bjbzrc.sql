-- IT 3380 Final Project SQL views
-- by Brandon Buttlar, BJBZRC

-- 1. Write a query to create a view named “EmployeesPerRegion” that shows the 
-- region_name and the number of employees from that region in
-- a column called “Number of Employees”. 
CREATE VIEW EmployeesPerRegion AS
SELECT r.region_name, COUNT(e.employee_id) As "Number of Employees"
FROM employees e
JOIN departments d ON d.department_id = e.department_id
JOIN locations l ON l.location_id = d.location_id
JOIN countries c ON c.country_id = l.country_id
JOIN regions r ON r.region_id = c.region_id
GROUP BY r.region_id;

-- 2. Write a query to create a view named “managers” to display all the managers.
-- Include the manager’s name (first, last), phone number, email, job title, and department name.
CREATE VIEW managers AS
SELECT e.first_name, e.last_name, e.phone_number, e.email, j.job_title, d.department_name
FROM employees e, departments d, jobs j
WHERE e.department_id = d.department_id AND e.job_id = j.job_id AND e.employee_id IN (SELECT manager_id from employees);

-- 3. Write a query to create a view named “DependentsByDepartment” to get
-- a count of how many dependents there are in each department.
CREATE VIEW DependentsByDepartment AS
SELECT d.department_name, COUNT(de.dependent_id) AS "Number of Dependents"
FROM dependents de
JOIN employees e ON e.employee_id = de.employee_id
JOIN departments d ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY COUNT(de.dependent_id) DESC;

-- 4. Write a query to create a view named “HiresByYear” that calculates
-- the number of employees hired each year.
CREATE VIEW HiresByYear AS  
SELECT YEAR(hire_date) AS "year", COUNT(employee_id) AS "Employees Hired"
FROM employees
GROUP BY YEAR(hire_date);

-- 5. Write a query to create a view named “SalaryByDepartment”
-- to calculate total salaries for each department. 
CREATE VIEW SalaryByDepartment AS
SELECT d.department_name, SUM(e.salary) AS "Total Salary"
FROM departments d, employees e
WHERE e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY SUM(e.salary) DESC;

-- 6. Write a query to create a view named “SalaryByJobTitle”
-- to calculate total salaries for each job title. 
CREATE VIEW SalaryByJobTitle AS
SELECT j.job_title, SUM(e.salary) AS "Total Salary"
FROM jobs j, employees e
WHERE e.job_id = j.job_id
GROUP BY j.job_title
ORDER BY SUM(e.salary) DESC;

-- 7. Write a query to create a view named “EmployeeDependents” that
-- calculates the number of dependents each employees has.
CREATE VIEW EmployeeDependents AS
SELECT e.first_name, e.last_name, e.email, e.phone_number, COUNT(d.dependent_id) AS "Number of Dependents"
FROM employees e
LEFT JOIN dependents d ON d.employee_id = e.employee_id
GROUP BY e.employee_id;

-- 8. Write a query to create a view named “CountryLocation”
-- that calculates the number of locations in each country.
CREATE VIEW CountryLocation AS
SELECT c.country_name, COUNT(l.location_id) AS "Number of Locations"
FROM countries c
LEFT JOIN locations l ON c.country_id = l.country_id
GROUP BY c.country_name;
