### HR DATA ANALYSIS - SQL SERVER / POWER BI

This project explores human resource data analysis using SQL and Power BI, aimed at revealing key insights to aid company decisions.

## Source Data:
The dataset includes HR records of 22,000 employees from 2000 to 2020.

## Data Cleaning & Analysis:

- Data loading & inspection
- Handling missing values
- Data cleaning and transformation

## Data Visualization:
Power BI Desktop

## Exploratory Data Analysis
### Questions:

1.**What's the age distribution in the company in both Gregorian and Persian calendars?**
2.**What's the gender breakdown in the company?
3. **How does gender vary across departments and job titles?
4. **What's the race distribution in the company?
5. **What's the average length of employment in the company?
6. **Which department has the highest turnover rate?
7. **What is the tenure distribution for each department?
8. **How many employees work remotely for each department?
9. **What's the distribution of employees across different states?
10. **How are job titles distributed in the company?
11. **How have employee hire counts varied over time?
12. **What's the salary distribution by department?
13. **What are the most common reasons for employee termination?
14. **How does the average age at hire vary by department?
15. **How many employees have transferred departments?
16. **What is the retention rate over the last 5 years?

### Insights:
1. **Age Distribution**:
   - Convert birthdate and termdate to the Persian calendar.
   - Analyze age distribution in both Gregorian and Persian calendars.
2. **Employee Satisfaction**:
   - Examine how satisfaction levels differ by department.
   - Identify job titles with the highest satisfaction ratings.
3. **Educational Qualifications**:
   - Assess the distribution of educational qualifications.
4. **Salary Trends**:
   - Track changes in average salary over time.
5. **Performance and Tenure**:
   - Correlate tenure with job performance ratings.
6. **Department Tenure**:
   - Compare average tenure across departments.
7. **Promotion Analysis**:
   - Count the number of promotions each year.
8. **Marital Status**:
   - Analyze the distribution of employees by marital status.
9. **Retirement Eligibility**:
   - Identify employees eligible for retirement soon.
10. **Diversity Analysis**:
   - Calculate and compare diversity indices across states.

### Implementation Steps:

### 1) Create Database
```sql
CREATE DATABASE hr;
```

### 2) Import Data to SQL Server
- Right-click on Human_Resources > Tasks > Import Data
- Use import wizard to import HR Data.csv to hr table.
- Verify that the import worked:

```sql
USE hr;
SELECT * FROM hr_data;
```

### 3)  Data Cleaning and Transformation Steps

#### Ensure data types are consistent
```sql
-- Convert hire_date and birthdate to date types if they aren't already
ALTER TABLE hr_data
ALTER COLUMN hire_date DATE;

ALTER TABLE hr_data
ALTER COLUMN birthdate DATE;
```

#### Add columns for additional analysis
```sql
-- Add columns for calculating tenure and job performance ratings
ALTER TABLE hr_data
ADD tenure INT,
    job_performance_rating FLOAT;
```

#### Populate the new columns
```sql
-- Calculate tenure
UPDATE hr_data
SET tenure = DATEDIFF(YEAR, hire_date, COALESCE(new_termdate, GETDATE()));

-- Example: Assume job performance ratings are calculated based on some criteria
-- This is just a placeholder; replace with actual logic
UPDATE hr_data
SET job_performance_rating = (CASE
    WHEN job_performance IS NOT NULL THEN job_performance * 1.0
    ELSE 0.0
END);
```

#### Update date/time to date format
- Convert dates to yyyy-MM-dd
- Create new columns for Persian dates

```sql
UPDATE hr_data
SET termdate = FORMAT(CONVERT(DATETIME, LEFT(termdate, 19), 120), 'yyyy-MM-dd');

ALTER TABLE hr_data
ADD new_termdate DATE;

UPDATE hr_data
SET new_termdate = CASE
    WHEN termdate IS NOT NULL AND ISDATE(termdate) = 1 THEN CAST(termdate AS DATETIME) ELSE NULL
END;

SELECT new_termdate FROM hr_data;
```

#### Create new columns for age and Persian dates
```sql
ALTER TABLE hr_data
ADD age INT, persian_birthdate NVARCHAR(10), persian_termdate NVARCHAR(10);

UPDATE hr_data
SET age = DATEDIFF(YEAR, birthdate, GETDATE());
```

#### Define a function to convert Gregorian dates to Persian dates
```sql
CREATE FUNCTION dbo.GregorianToPersian (@gregorianDate DATE)
RETURNS NVARCHAR(10)
AS
BEGIN
    DECLARE @persianDate NVARCHAR(10);
    -- Placeholder conversion logic; replace with actual conversion logic
    SET @persianDate = CONVERT(NVARCHAR(10), @gregorianDate, 111);
    RETURN @persianDate;
END;

UPDATE hr_data
SET persian_birthdate = dbo.GregorianToPersian(birthdate),
    persian_termdate = dbo.GregorianToPersian(termdate);
```

### QUESTIONS TO ANSWER FROM THE DATA

#### 1) What's the age distribution in the company?
```sql
SELECT MIN(age) AS youngest, MAX(age) AS oldest FROM hr_data;

SELECT age_group, COUNT(*) AS count
FROM (
    SELECT 
        CASE
            WHEN age <= 21 THEN '21 to 30'
            WHEN age BETWEEN 31 AND 40 THEN '31 to 40'
            WHEN age BETWEEN 41 AND 50 THEN '41 to 50'
            ELSE '50+'
        END AS age_group
    FROM hr_data
    WHERE new_termdate IS NULL
) AS subquery
GROUP BY age_group
ORDER BY age_group;
```

#### 2) How does employee satisfaction vary across departments?
```sql
SELECT department, AVG(employee_satisfaction) AS avg_satisfaction
FROM hr_data
GROUP BY department
ORDER BY avg_satisfaction DESC;
```

#### 3) Top 5 job titles with highest employee satisfaction
```sql
SELECT jobtitle, AVG(employee_satisfaction) AS avg_satisfaction
FROM hr_data
GROUP BY jobtitle
ORDER BY avg_satisfaction DESC
LIMIT 5;
```

#### 4) Distribution of educational qualifications
```sql
SELECT education_level, COUNT(*) AS count
FROM hr_data
GROUP BY education_level
ORDER BY count DESC;
```

#### 5) Average salary change over the years
```sql
SELECT YEAR(hire_date) AS hire_year, AVG(salary) AS avg_salary
FROM hr_data
GROUP BY YEAR(hire_date)
ORDER BY hire_year;
```

#### 6) Correlation between tenure and job performance ratings
```sql
SELECT DATEDIFF(YEAR, hire_date, COALESCE(termdate, GETDATE())) AS tenure, AVG(job_performance) AS avg_performance
FROM hr_data
GROUP BY DATEDIFF(YEAR, hire_date, COALESCE(termdate, GETDATE()))
ORDER BY tenure;
```

#### 7) Average tenure by department
```sql
SELECT department, AVG(DATEDIFF(YEAR, hire_date, COALESCE(termdate, GETDATE()))) AS avg_tenure
FROM hr_data
GROUP BY department
ORDER BY avg_tenure DESC;
```

#### 8) Number of promotions each year
```sql
SELECT YEAR(promotion_date) AS promotion_year, COUNT(*) AS promotions
FROM hr_data
WHERE promotion_date IS NOT NULL
GROUP BY YEAR(promotion_date)
ORDER BY promotion_year;
```

#### 9) Distribution by marital status
```sql
SELECT marital_status, COUNT(*) AS count
FROM hr_data
GROUP BY marital_status
ORDER BY count DESC;
```

#### 10) Employees eligible for retirement in the next 5 years
```sql
SELECT COUNT(*) AS eligible_for_retirement
FROM hr_data
WHERE DATEDIFF(YEAR, birthdate, GETDATE()) >= 55;
```

#### 11) Diversity index by state
```sql
SELECT location_state, 
       1.0 / SUM(CAST(COUNT(race) AS FLOAT) / (SELECT COUNT(*) FROM hr_data WHERE new_termdate IS NULL)) AS diversity_index
FROM hr_data
WHERE new_termdate IS NULL
GROUP BY location_state
ORDER BY diversity_index DESC;
```
### Additional Exploratory Data Analysis (EDA)

#### 12) What's the salary distribution by department?
```sql
SELECT department, 
       PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS Q1,
       PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY salary) AS median,
       PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS Q3
FROM hr_data
GROUP BY department
ORDER BY department;
```

#### 13) What are the most common reasons for employee termination?
```sql
SELECT termination_reason, COUNT(*) AS count
FROM hr_data
WHERE new_termdate IS NOT NULL
GROUP BY termination_reason
ORDER BY count DESC;
```

#### 14) How does the average age at hire vary by department?
```sql
SELECT department, AVG(DATEDIFF(YEAR, birthdate, hire_date)) AS avg_age_at_hire
FROM hr_data
GROUP BY department
ORDER BY avg_age_at_hire;
```

#### 15) How many employees have transferred departments?
```sql
SELECT COUNT(DISTINCT employee_id) AS transfer_count
FROM hr_data
WHERE department_transfer_date IS NOT NULL;
```

#### 16) What is the retention rate over the last 5 years?
```sql
SELECT hire_year, 
       COUNT(*) AS hires, 
       SUM(CASE WHEN new_termdate IS NULL THEN 1 ELSE 0 END) AS retained
FROM (
    SELECT YEAR(hire_date) AS hire_year, new_termdate
    FROM hr_data
) AS subquery
WHERE hire_year >= YEAR(GETDATE()) - 5
GROUP BY hire_year
ORDER BY hire_year;
```

### Data Visualization Ideas for Power BI

#### Dashboard Components:
1. **Age Distribution Chart**: Bar chart showing age distribution in both Gregorian and Persian calendars.
2. **Employee Satisfaction by Department**: Heat map highlighting departments with varying satisfaction levels.
3. **Educational Qualification Distribution**: Pie chart displaying the distribution of educational qualifications.
4. **Average Salary Over Time**: Line graph tracking average salary changes year over year.
5. **Performance vs. Tenure Scatter Plot**: Scatter plot to show the correlation between tenure and job performance ratings.
6. **Tenure by Department**: Bar chart comparing average tenure across different departments.
7. **Promotion Trends**: Line chart showing the number of promotions each year.
8. **Marital Status Distribution**: Pie chart showing the distribution of employees by marital status.
9. **Retirement Eligibility**: Bar chart indicating the number of employees eligible for retirement in the next 5 years.
10. **Diversity Index by State**: Map visualization showing the diversity index across different states.
11. **Salary Distribution by Department**: Box plot visualizing the salary range within each department.
12. **Termination Reasons**: Bar chart showing the most common reasons for employee termination.
13. **Age at Hire by Department**: Bar chart illustrating the average age at hire for each department.
14. **Department Transfers**: Line graph indicating the number of department transfers over the years.
15. **Retention Rate**: Stacked bar chart showing retention rates over the last 5 years.

### Summary:
By following these steps, you can enhance your HR data analysis project with new questions and insights, ensuring that it stands out in your portfolio. The added analysis and visualizations provide a more comprehensive understanding of the HR data, showcasing your skills in SQL and Power BI effectively.
