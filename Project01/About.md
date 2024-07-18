## **Human Resource DATA ANALYSIS** ##
### SQL SERVER / POWER BI ###

This project explores human resource data analysis using SQL and Power BI, aimed at revealing key insights to aid company decisions.

## Source Data:
The dataset includes HR records of 22,000 employees from 2000 to 2020.

## Data Cleaning & Analysis:

- Data loading & inspection
- Handling missing values
- Data cleaning and transformation

## Data Visualization:
Power BI Desktop

## Source Data:
The dataset includes HR records of 22,000 employees from 2000 to 2020.

## Data Cleaning & Analysis:

- Data loading & inspection
- Handling missing values
- Data cleaning and transformation

## Data Visualization:
Power BI Desktop

## Exploratory Data Analysis
## Questions:
1. **What's the age distribution in the company?**
2. **What's the gender breakdown in the company?**
3. **How does gender vary across departments and job titles?**
4. **What's the race distribution in the company?**
5. **What's the average length of employment in the company?**
6. **Which department has the highest turnover rate?**
7. **What is the tenure distribution for each department?**
8. **How many employees work remotely for each department?**
9. **What's the distribution of employees across different states?**
10. **How are job titles distributed in the company?**
11. **How have employee hire counts varied over time?**
12. **What is the average tenure of employees who work remotely compared to those who do not?**
13. **What are the most common reasons for employee termination?**
14. **Which job titles have the highest and lowest average tenure?**
15. **How does the age of employees correlate with their job title and department?**
16. **What is the distribution of employees' hire dates over the 20-year period?**
17. **How do termination rates vary by race and gender?**
18. **What is the distribution of employees by city and department?**

## Insights:
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
   - 
## **Data Cleaning and Transformation Steps**
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
- Create new columns for age

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
#### Additional Data Cleaning Steps:
- Convert salary and performance-related columns to appropriate data types if necessary.
- Handle missing values in educational qualification and performance columns.
- Create new columns for Persian dates

## **QUESTIONS TO ANSWER FROM THE DATA**

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
#### 12) What's the distribution of educational qualifications among employees?
```sql
SELECT
  education_level,
  COUNT(*) AS count
FROM
  hr_data
WHERE
  new_termdate IS NULL
GROUP BY
  education_level
ORDER BY
  count DESC;
```

#### 13) How does the average salary differ across departments and job titles?
```sql
SELECT
  department,
  jobtitle,
  AVG(salary) AS average_salary
FROM
  hr_data
WHERE
  new_termdate IS NULL
GROUP BY
  department, jobtitle
ORDER BY
  average_salary DESC;
```

#### 14) What is the correlation between employee age and job level?
```sql
SELECT
  age,
  job_level,
  COUNT(*) AS count
FROM
  hr_data
WHERE
  new_termdate IS NULL
GROUP BY
  age, job_level
ORDER BY
  age, job_level;
```

#### 15) Which departments have the highest promotion rates?
```sql
SELECT
  department,
  COUNT(*) AS promotion_count
FROM
  hr_data
WHERE
  promoted = 1
GROUP BY
  department
ORDER BY
  promotion_count DESC;
```

#### 16) How does employee performance vary by department and job title?
```sql
SELECT
  department,
  jobtitle,
  AVG(performance_score) AS average_performance
FROM
  hr_data
WHERE
  new_termdate IS NULL
GROUP BY
  department, jobtitle
ORDER BY
  average_performance DESC;
```

#### 17) What are the reasons for termination and their distribution across departments?
```sql
SELECT
  department,
  termination_reason,
  COUNT(*) AS count
FROM
  hr_data
WHERE
  new_termdate IS NOT NULL
GROUP BY
  department, termination_reason
ORDER BY
  count DESC;
```

## **Data Visualization Ideas for Power BI**
### **Findings**
1. The age distribution shows a majority of employees are between 31-50 years old.
2. Gender distribution indicates a slight male majority.
3. Gender variation across departments and job titles is relatively balanced.
4. Caucasians are the majority race in the company.
5. The average employment length is approximately 7 years.
6. The Auditing department has the highest turnover rate.
7. Tenure is fairly evenly distributed across departments.
8. About 25% of employees work remotely.
9. Most employees are based in Ohio.
10. Research Assistant II is the most common job title.
11. Employee hire counts have increased over the years.
12. Employees working remotely have a slightly higher average tenure compared to those who do not.
13. Personal reasons are the most common reason for employee termination.
14. Executive-level job titles have the highest average tenure, while entry-level job titles have the lowest.
15. Older employees tend to hold higher-level job titles and are concentrated in certain departments like Management and Research.
16. The majority of hires occurred between 2010 and 2020, with a noticeable increase in recent years.
17. Termination rates are higher among certain racial groups and show slight gender variation.
18. Cities with the highest employee counts also have diverse departmental representatio

### **Dashboard Components**
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
