### 📊 Superstore Sales Data Analysis with SQL

---

### 📜 Overview
This project showcases the use of SQL for analyzing **Superstore Sales Dataset**, uncovering key trends, and measuring business performance metrics. The analysis aims to derive actionable insights that support data-driven decision-making.

---

### 🛠️ Key Skills and Tools
- **SQL**: Aggregations, Joins, Subqueries, Common Table Expressions (CTEs)
- **Data Analysis**: Revenue trends, top-selling products, customer segmentation, regional performance
- **Database Management**: Efficient handling of relational databases with large datasets
- **Visualization**: Interactive and actionable charts using Power BI

---

### 🔑 Highlights
- **Comprehensive Analysis**: Covers revenue trends, customer behavior, and performance across regions and categories.
- **KPIs Measured**: Total sales, revenue growth, Average Order Value (AOV), and Customer Segmentation.
- **Advanced SQL Techniques**:  
  - Window functions for cumulative calculations  
  - Correlated subqueries for detailed insights  
  - CTEs for modular and reusable queries  

---

### 🗂️ Data Description
#### Data Schema
1. **Customers Table**  
   - `CustomerID`: Unique identifier for each customer  
   - `CustomerName`: Name of the customer  
   - `Region`: Geographic region  
   - `Segment`: Customer segment (e.g., Consumer, Corporate, Home Office)

2. **Orders Table**  
   - `OrderID`: Unique order identifier  
   - `OrderDate`: Date when the order was placed  
   - `ShipDate`: Date when the order was shipped  
   - `CustomerID`: Foreign key linking to the Customers table  
   - `ShipMode`: Shipping mode of the order  

3. **Products Table**  
   - `ProductID`: Unique identifier for each product  
   - `ProductName`: Name of the product  
   - `Category`: Product category (e.g., Furniture, Technology, Office Supplies)  
   - `SubCategory`: Sub-category of the product  

4. **Sales Table**  
   - `OrderID`: Foreign key linking to the Orders table  
   - `ProductID`: Foreign key linking to the Products table  
   - `Sales`: Amount of sales  

---

### 🧰 Steps in the Analysis
1. **Data Cleaning**  
   - Resolved missing or inconsistent data using SQL functions  
   - Standardized date formats and resolved duplicate entries  

2. **Exploratory Data Analysis (EDA)**  
   - Analyzed revenue distribution across regions and categories  
   - Studied sales performance over time  
   - Identified high-performing products and customer segments  

3. **KPI Calculations**  
   - Total revenue and revenue growth rates  
   - Average Order Value (AOV)  
   - Customer segmentation based on spending  

4. **Actionable Insights**  
   - Identified top-performing regions, products, and seasonal trends  
   - Suggested strategies for inventory management and marketing  

---

### 📂 Repository Contents
#### 1. SQL Scripts  
Collection of SQL queries for analyzing sales data:  
- **1.1 Total Sales by Region**
```sql
SELECT 
    c.Region, 
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.Region
ORDER BY TotalSales DESC;
```

- **1.2 Monthly Revenue Trends**
```sql
SELECT 
    FORMAT(OrderDate, 'yyyy-MM') AS Month,
    SUM(Sales) AS MonthlyRevenue
FROM Sales
JOIN Orders ON Sales.OrderID = Orders.OrderID
GROUP BY FORMAT(OrderDate, 'yyyy-MM')
ORDER BY Month;
```

- **1.3 Top-Selling Products**
```sql
SELECT 
    ProductName,
    SUM(Sales) AS TotalRevenue
FROM Sales
JOIN Products ON Sales.ProductID = Products.ProductID
GROUP BY ProductName
ORDER BY TotalRevenue DESC
LIMIT 10;
```

- **1.4 Customer Segmentation by Spending**
```sql
SELECT 
    CustomerName,
    CASE 
        WHEN SUM(Sales) >= 2000 THEN 'High Spender'
        WHEN SUM(Sales) >= 1000 THEN 'Medium Spender'
        ELSE 'Low Spender'
    END AS SpendingCategory,
    SUM(Sales) AS TotalSpent
FROM Sales
JOIN Customers ON Sales.CustomerID = Customers.CustomerID
GROUP BY CustomerName
ORDER BY TotalSpent DESC;
```

- **1.5 Sales Performance by Category**
```sql
SELECT 
    Category,
    SUM(Sales) AS TotalSales
FROM Sales
JOIN Products ON Sales.ProductID = Products.ProductID
GROUP BY Category
ORDER BY TotalSales DESC;
```

#### 2. Data  
Sample datasets:  
- `customers.csv`  
- `orders.csv`  
- `products.csv`  
- `sales.csv`  

#### 3. Analysis Report  
A PDF report summarizing key findings:  
- Revenue trends over time  
- Best and worst-performing products  
- Regional sales performance  
- Customer segmentation insights  

#### 4. Power BI Dashboard  
Interactive Power BI file (`.pbix`) visualizing:  
- Revenue Trends: Line chart for monthly revenue  
- Top Products: Bar chart for best-selling products  
- Regional Performance: Heatmap for revenue distribution by region  
- Customer Segmentation: Pie chart for customer spending categories  

---

### 🎯 Business Objectives
- **Identify growth opportunities** in underperforming regions  
- **Optimize inventory management** for high-demand products  
- **Develop targeted marketing strategies** based on customer segmentation  
