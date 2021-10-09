-- Salaries Differences
-- Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
-- Output just the difference in salaries.
select t2.max_salary-LAG(t2.max_salary, 1) OVER(ORDER BY t2.max_salary) as salary_difference
from 
(select t.department, max(t.salary) as max_salary from
    (select * from db_employee e 
    join db_dept d 
    on e.department_id = d.id
    where d.department in ('marketing', 'engineering')) as t
group by t.department
order by max_salary desc) as t2
offset 1;
