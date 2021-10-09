# SQL Window Functions

## Window Functions
- Window functions perform calculations on a set of rows that are related together. 
- But, unlike the aggregate functions, windowing functions do not collapse the result of the rows into a single value. 
- Instead, `all the rows maintain their original identity and the calculated result is returned for every row`.

### OVER clause
- The OVER clause signifies a window of rows over which a window function is applied.

To display the total salary of employees along with every row value:
```sql
select *
    , sum(salary) OVER() as total_salary
from emp;
```

### PARTITION BY clause
The PARTITION BY clause is used in conjunction with the OVER clause. It breaks up the rows into different partitions. These partitions are then acted upon by the window function.

To display the total salary per job category for all the rows:
```sql
select *
    , sum(salary) OVER(PARTITION BY job) as total_job_salary
from emp;
```

### Arranging Rows within Partitions
To arrange rows within each partition, include the ORDER BY clause with the OVER clause.
```sql
select *
    , sum(salary) OVER(PARTITION BY job ORDER BY salary desc) as running_total_job_salary
from emp;
```

### ROW_NUMBER
ROW_NUMBER() window function assigns a unique sequential number to each row of the table.
```sql
select *
    , ROW_NUMBER() OVER() as row_number
from emp;
```

```sql
select *
    , ROW_NUMBER() OVER(PARTITION BY job ORDER BY salary) as row_number
from emp;
```

### RANK
The RANK() window function ranks the rows within their partition based on the given condition.
```sql
select *
    , ROW_NUMBER() OVER(PARTITION BY job ORDER BY salary) as row_number,
    , RANK() OVER(PARTITION BY job ORDER BY salary) as rank_row
from emp;
```

### DENSE_RANK
The DENSE_RANK() function is similar to the RANK() except that, it doesn’t skip any ranks when ranking rows.
```sql
select *
    , ROW_NUMBER() OVER(PARTITION BY job ORDER BY salary) as row_number,
    , RANK() OVER(PARTITION BY job ORDER BY salary) as rank_row
    , DENSE_RANK() OVER(PARTITION BY job ORDER BY salary) as dense_rank_row
from emp;
```

### Nth_Value
If you want to retrieve the nth value from a window frame for an expression, then you can use the `NTH_VALUE(expression, N)` window function.

For example, to retrieve the third-highest salary in each JOB category, we can partition the rows according to the JOB column, then order the rows within the partitions according to decreasing salary, and finally, use the NTH_VALUE function to retrieve the value.
```sql
select *
    , NTH_VALUE(name, 3) OVER(PARTITION BY job ORDER BY salary RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as third
```

### NTILE
This is useful when you want to determine the percentile, quartile, etc. a particular row falls into. The NTILE() function is used for such purposes. It returns the group number for each of the rows in the partition.
```sql
select *
    , NTILE(4) OVER(ORDER BY salary) as quartile
from emp
```

### LEAD() and LAG()
- To compare the value of the current row to that of the preceding or succeeding row.

To create a new column containing SALARY from the next row within each partition ordered by salary:
```sql
select *
    , LEAD(salary, 1) OVER(PARTITION BY job ORDER BY salary) as next_salary
from emp
```
```sql
select *
    , LAG(salary, 1) OVER(PARTITION BY job ORDER BY salary) as previous_salary
    , salary - LAG(salary, 1) OVER(PARTITION BY job ORDER BY salary) as sal_diff
from emp
```