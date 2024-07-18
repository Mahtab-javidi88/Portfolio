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
13. **Which job titles have the highest and lowest average tenure?**
14. **How does the age of employees correlate with their job title and department?**
15. **What is the distribution of employees' hire dates over the 20-year period?**
16. **How do termination rates vary by race and gender?**
17. **What is the distribution of employees by city and department?**
18. **What is the average age of employees at the time of hiring?**

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
#### Fixes zero values from the above query
```sql
SELECT
    hire_yr,
    hires,
    terminations,
    hires - terminations AS net_change,
    (round(CAST(hires - terminations AS FLOAT) / NULLIF(hires, 0), 2)) *100 AS percent_hire_change
FROM  
    (SELECT
        YEAR(hire_date) AS hire_yr,
        COUNT(*) AS hires,
        SUM(CASE WHEN new_termdate IS NOT NULL AND new_termdate <= GETDATE() THEN 1 ELSE 0 END) terminations
    FROM hr_data
    GROUP BY YEAR(hire_date)
    ) AS subquery
ORDER BY hire_yr ASC;
```
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
- Calculate tenure
```sql
UPDATE hr_data
SET tenure = DATEDIFF(YEAR, hire_date, COALESCE(new_termdate, GETDATE()));

- Example: Assume job performance ratings are calculated based on some criteria
- This is just a placeholder; replace with actual logic
```sql
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

#### Create new columns for Persian dates
- Define a function to convert Gregorian dates to Persian dates
```sql
CREATE FUNCTION dbo.PersianDayOfYear (
    @Year INT,
    @Month INT,
    @Day INT
)
RETURNS INT
AS
BEGIN
    DECLARE @DayOfYear INT;

    IF @Month < 7
        SET @DayOfYear = (@Month - 1) * 31 + @Day;
    ELSE
        SET @DayOfYear = 6 * 31 + (@Month - 7) * 30 + @Day;

    RETURN @DayOfYear;
END;
GO
```
#### Helping Function for Calculating KABISE
```sql
CREATE FUNCTION dbo.IsPersianLeapYear (
    @Year INT
)
RETURNS BIT
AS
BEGIN
    RETURN CASE
        WHEN ((@Year - 474) % 2820 + 474 + 38) * 682 % 2816 < 682 THEN 1
        ELSE 0
    END;
END;
GO
```
#### Main Function For Converting Date to Jalali
```sql
CREATE FUNCTION dbo.GregorianToPersian (
    @GregorianDate DATE
)
RETURNS NVARCHAR(10)
AS
BEGIN
    DECLARE @Gy INT, @Gm INT, @Gd INT;
    DECLARE @Jy INT, @Jm INT, @Jd INT;
    DECLARE @DayNo INT, @PersianNewYearDayNo INT;
    DECLARE @PersianDate NVARCHAR(10);
    DECLARE @LeapYear BIT;

    
    SET @Gy = YEAR(@GregorianDate);
    SET @Gm = MONTH(@GregorianDate);
    SET @Gd = DAY(@GregorianDate);

    SET @DayNo = DATEDIFF(DAY, CONVERT(DATE, CONCAT(@Gy, '-01-01')), @GregorianDate) + 1;

    SET @LeapYear = dbo.IsPersianLeapYear(@Gy - 621);
    SET @PersianNewYearDayNo = CASE WHEN @LeapYear = 1 THEN 80 ELSE 79 END;

    IF @DayNo > @PersianNewYearDayNo
    BEGIN
        SET @DayNo = @DayNo - @PersianNewYearDayNo;
        SET @Jy = @Gy - 621;
    END
    ELSE
    BEGIN
        SET @DayNo = @DayNo + CASE WHEN dbo.IsPersianLeapYear(@Gy - 622) = 1 THEN 366 ELSE 365 END - @PersianNewYearDayNo;
        SET @Jy = @Gy - 622;
    END;

  
    IF @DayNo <= 186
    BEGIN
        SET @Jm = CEILING(@DayNo / 31.0);
        SET @Jd = @DayNo - (@Jm - 1) * 31;
    END
    ELSE
    BEGIN
        SET @Jm = CEILING((@DayNo - 186) / 30.0) + 6;
        SET @Jd = @DayNo - 186 - (@Jm - 7) * 30;
    END;

    
    SET @PersianDate = FORMAT(@Jy, '0000') + '-' + FORMAT(@Jm, '00') + '-' + FORMAT(@Jd, '00');

    RETURN @PersianDate;
END;
GO
```

#### Create new columns for Persian dates
```sql
UPDATE hr_data
SET persian_birthdate = dbo.GregorianToPersian(birthdate)

ALTER TABLE hr_data
ADD persian_Hiredate NVARCHAR(10)
UPDATE hr_data
SET persian_Hiredate = dbo.GregorianToPersian(hire_date);

--view age and Persian dates
SELECT birthdate,persian_birthdate,age,hire_date,persian_Hiredate
FROM hr_data
```
## Handling Missing Values and Performance Analysis

### Data Cleaning Steps:
1. **Inspect Data for Missing Values:**
    - Identify columns with missing values.
    - Determine the appropriate strategy to handle missing values (e.g., imputation, removal).

2. **Handle Missing Values:**
    - For numerical columns, you can fill missing values with the mean or median.
    - For categorical columns, you can fill missing values with the mode or create a new category like "Unknown".
    - Remove rows with missing values if necessary.

### SQL Queries for Handling Missing Values:
To handle missing values in the dataset and focus on performance columns, you can follow these steps. These include data cleaning, handling missing values, and analyzing key performance metrics. Here is a detailed outline:

#### Identify Missing Values:
```sql
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN birthdate IS NULL THEN 1 ELSE 0 END) AS missing_birthdate,
    SUM(CASE WHEN gender IS NULL THEN 1 ELSE 0 END) AS missing_gender,
    SUM(CASE WHEN race IS NULL THEN 1 ELSE 0 END) AS missing_race,
    SUM(CASE WHEN department IS NULL THEN 1 ELSE 0 END) AS missing_department,
    SUM(CASE WHEN jobtitle IS NULL THEN 1 ELSE 0 END) AS missing_jobtitle,
    SUM(CASE WHEN location IS NULL THEN 1 ELSE 0 END) AS missing_location,
    SUM(CASE WHEN hire_date IS NULL THEN 1 ELSE 0 END) AS missing_hire_date,
    SUM(CASE WHEN termdate IS NULL THEN 1 ELSE 0 END) AS missing_termdate,
    SUM(CASE WHEN location_city IS NULL THEN 1 ELSE 0 END) AS missing_location_city,
    SUM(CASE WHEN location_state IS NULL THEN 1 ELSE 0 END) AS missing_location_state
FROM hr_data;
```

#### Fill Missing Values for Numerical Columns:
```sql
-- Example: Filling missing age with the average age
UPDATE hr_data
SET age = (SELECT AVG(age) FROM hr_data)
WHERE age IS NULL;
```

#### Fill Missing Values for Categorical Columns:
```sql
-- Example: Filling missing gender with the mode
UPDATE hr_data
SET gender = (SELECT TOP 1 gender FROM hr_data GROUP BY gender ORDER BY COUNT(*) DESC)
WHERE gender IS NULL;
```

#### Remove Rows with Missing Critical Values:
```sql
-- Example: Removing rows with missing hire_date
DELETE FROM hr_data
WHERE hire_date IS NULL;
```

### Analyzing Performance Metrics:
Focus on columns related to performance, such as tenure, age, department, and job title.

### SQL Queries for Performance Analysis:
#### Calculate Average Tenure:
```sql
SELECT 
    AVG(DATEDIFF(year, hire_date, ISNULL(new_termdate, GETDATE()))) AS average_tenure
FROM 
    hr_data;
```

#### Average Tenure by Department:
```sql
SELECT 
    department,
    AVG(DATEDIFF(year, hire_date, ISNULL(new_termdate, GETDATE()))) AS average_tenure
FROM 
    hr_data
GROUP BY 
    department;
```

#### Average Tenure by Job Title:
```sql
SELECT 
    jobtitle,
    AVG(DATEDIFF(year, hire_date, ISNULL(new_termdate, GETDATE()))) AS average_tenure
FROM 
    hr_data
GROUP BY 
    jobtitle;
```

#### Age Distribution:
```sql
SELECT 
    CASE 
        WHEN age <= 20 THEN '20 and below'
        WHEN age BETWEEN 21 AND 30 THEN '21-30'
        WHEN age BETWEEN 31 AND 40 THEN '31-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        ELSE '51 and above'
    END AS age_group,
    COUNT(*) AS count
FROM 
    hr_data
GROUP BY 
    CASE 
        WHEN age <= 20 THEN '20 and below'
        WHEN age BETWEEN 21 AND 30 THEN '21-30'
        WHEN age BETWEEN 31 AND 40 THEN '31-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        ELSE '51 and above'
    END;
```

#### Performance by Location:
```sql
SELECT 
    location,
    COUNT(*) AS employee_count,
    AVG(DATEDIFF(year, hire_date, ISNULL(new_termdate, GETDATE()))) AS average_tenure
FROM 
    hr_data
GROUP BY 
    location;
```


## **QUESTIONS TO ANSWER FROM THE DATA**

#### 1. What's the age distribution in the company?
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

#### 2. How does employee satisfaction vary across departments?
```sql
SELECT department, AVG(employee_satisfaction) AS avg_satisfaction
FROM hr_data
GROUP BY department
ORDER BY avg_satisfaction DESC;
```

#### 3. Top 5 job titles with highest employee satisfaction
```sql
SELECT jobtitle, AVG(employee_satisfaction) AS avg_satisfaction
FROM hr_data
GROUP BY jobtitle
ORDER BY avg_satisfaction DESC
LIMIT 5;
```

#### 4. Distribution of educational qualifications
```sql
SELECT education_level, COUNT(*) AS count
FROM hr_data
GROUP BY education_level
ORDER BY count DESC;
```

#### 5. Average salary change over the years
```sql
SELECT YEAR(hire_date) AS hire_year, AVG(salary) AS avg_salary
FROM hr_data
GROUP BY YEAR(hire_date)
ORDER BY hire_year;
```

#### 6. Correlation between tenure and job performance ratings
```sql
SELECT DATEDIFF(YEAR, hire_date, COALESCE(termdate, GETDATE())) AS tenure, AVG(job_performance) AS avg_performance
FROM hr_data
GROUP BY DATEDIFF(YEAR, hire_date, COALESCE(termdate, GETDATE()))
ORDER BY tenure;
```

#### 7. Average tenure by department
```sql
SELECT department, AVG(DATEDIFF(YEAR, hire_date, COALESCE(termdate, GETDATE()))) AS avg_tenure
FROM hr_data
GROUP BY department
ORDER BY avg_tenure DESC;
```

#### 8. Number of promotions each year
```sql
SELECT YEAR(promotion_date) AS promotion_year, COUNT(*) AS promotions
FROM hr_data
WHERE promotion_date IS NOT NULL
GROUP BY YEAR(promotion_date)
ORDER BY promotion_year;
```

#### 9. Distribution by marital status
```sql
SELECT marital_status, COUNT(*) AS count
FROM hr_data
GROUP BY marital_status
ORDER BY count DESC;
```

#### 10. Employees eligible for retirement in the next 5 years
```sql
SELECT COUNT(*) AS eligible_for_retirement
FROM hr_data
WHERE DATEDIFF(YEAR, birthdate, GETDATE()) >= 55;
```

#### 11. Diversity index by state
```sql
SELECT location_state, 
       1.0 / SUM(CAST(COUNT(race) AS FLOAT) / (SELECT COUNT(*) FROM hr_data WHERE new_termdate IS NULL)) AS diversity_index
FROM hr_data
WHERE new_termdate IS NULL
GROUP BY location_state
ORDER BY diversity_index DESC;
```
#### 12. What is the average tenure of employees who work remotely compared to those who do not?
```sql
SELECT 
    location,
    AVG(DATEDIFF(year, hire_date, new_termdate)) AS average_tenure
FROM 
    hr_data
WHERE 
    new_termdate IS NOT NULL AND new_termdate <= GETDATE()
GROUP BY 
    location;
```

#### 12. What is the average tenure of employees who work remotely compared to those who do not?
```sql
SELECT 
    location,
    AVG(DATEDIFF(year, hire_date, new_termdate)) AS average_tenure
FROM 
    hr_data
WHERE 
    new_termdate IS NOT NULL AND new_termdate <= GETDATE()
GROUP BY 
    location;
```

#### 13. Which job titles have the highest and lowest average tenure?
```sql
SELECT
    jobtitle,
    AVG(DATEDIFF(year, hire_date, new_termdate)) AS average_tenure
FROM
    hr_data
WHERE
    new_termdate IS NOT NULL
GROUP BY
    jobtitle
ORDER BY
    average_tenure DESC;
```

#### 14. How does the age of employees correlate with their job title and department?
```sql
SELECT
    department,
    jobtitle,
    AVG(age) AS average_age
FROM
    hr_data
WHERE
    new_termdate IS NULL
GROUP BY
    department, jobtitle
ORDER BY
    department, jobtitle;
```

#### 15. What is the distribution of employees' hire dates over the 20-year period?
```sql
SELECT
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS count
FROM
    hr_data
GROUP BY
    YEAR(hire_date)
ORDER BY
    hire_year;
```

#### 16. How do termination rates vary by race and gender?
```sql
SELECT
    race,
    gender,
    COUNT(*) AS termination_count
FROM
    hr_data
WHERE
    new_termdate IS NOT NULL
GROUP BY
    race, gender
ORDER BY
    termination_count DESC;
```

#### 17. What is the distribution of employees by city and department?
```sql
SELECT
    location_city,
    department,
    COUNT(*) AS count
FROM
    hr_data
WHERE
    new_termdate IS NULL
GROUP BY
    location_city, department
ORDER BY
    count DESC;
```

#### 18. What is the average age of employees at the time of hiring?
```sql
SELECT 
    AVG(DATEDIFF(year, birthdate, hire_date)) AS average_hire_age
FROM 
    hr_data;
```


### **Findings and Dashboard Components**
1. **Age Distribution:** Majority of employees are between 31-50 years old.
2. **Gender Breakdown:** Slight male majority.
3. **Gender Variation:** Balanced across departments and job titles.
4. **Race Distribution:** Majority are Caucasian.
5. **Average Length of Employment:** Approximately 7 years.
6. **Department Turnover Rate:** Auditing has the highest turnover rate.
7. **Tenure Distribution:** Fairly even across departments.
8. **Remote Work:** About 25% of employees work remotely.
9. **State Distribution:** Most employees are based in Ohio.
10. **Job Titles:** Research Assistant II is the most common job title.
11. **Hire Counts Over Time:** Increased over the years.
12. **Remote vs. Non-Remote Tenure:** Remote employees have slightly higher average tenure.
13. **Job Title Tenure:** Executive-level job titles have the highest average tenure.
14. **Age Correlation:** Older employees tend to hold higher-level job titles.
15. **Hire Date Distribution:** Majority of hires occurred between 2010 and 2020.
16. **Termination Rates:** Higher among certain racial groups with slight gender variation.
17. **City and Department Distribution:** High employee counts in major cities with diverse departmental representation.
18. **Average Hiring Age:** Around 30 years old.

### Summary:
