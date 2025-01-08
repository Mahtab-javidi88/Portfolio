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

#### 1. SQL  Script Queries for Sales Data Analysis

### Total Sales of Each Product
```sql
SELECT 
    p.[Product Name],
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY TotalSales DESC;
```

---

### Calculate Average Sales per Customer
```sql
SELECT 
    c.[Customer Name],
    AVG(s.Sales) AS AverageSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.[Customer Name]
ORDER BY AverageSales DESC;
```

---

### Total Sales for Each Region
```sql
SELECT 
    c.Region,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.Region
ORDER BY TotalSales DESC;
```

---

### Top-Selling Products
```sql
SELECT TOP 10
    p.[Product Name],
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY TotalSales DESC;
```

---

### Top Customers by Sales
```sql
SELECT TOP 10
    c.[Customer Name],
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.[Customer Name]
ORDER BY TotalSales DESC;
```

---

### Total Sales for Each Month
```sql
SELECT 
    YEAR(o.[Order Date]) AS Year,
    MONTH(o.[Order Date]) AS Month,
    SUM(s.Sales) AS MonthlySales
FROM Orders o
JOIN Sales s ON o.[Order ID] = s.[Order ID]
GROUP BY YEAR(o.[Order Date]), MONTH(o.[Order Date])
ORDER BY Year, Month;
```

---

### Comparison of Sales in the Last Two Years
```sql
SELECT 
    YEAR([Order Date]) AS Year,
    SUM(Sales) AS TotalSales
FROM Sales
JOIN Orders ON Sales.[Order ID] = Orders.[Order ID]
WHERE YEAR([Order Date]) IN (
    SELECT DISTINCT TOP 2 YEAR([Order Date])
    FROM Orders
    ORDER BY YEAR([Order Date]) DESC
)
GROUP BY YEAR([Order Date])
ORDER BY Year;
```

---

### Identifying the Best-Selling Product Categories
```sql
SELECT 
    p.Category,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.Category
ORDER BY TotalSales DESC;
```

---

### Total Sales per State
```sql
SELECT 
    c.State,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.State
ORDER BY TotalSales DESC;
```

---

### Calculating Order Delivery Time for Each Order
```sql
SELECT 
    o.[Order ID],
    DATEDIFF(DAY, o.[Order Date], o.[Ship Date]) AS DeliveryTime
FROM Orders o
WHERE o.[Ship Date] IS NOT NULL
ORDER BY DeliveryTime DESC;
```

---

### Average Delivery Time
```sql
SELECT 
    AVG(DATEDIFF(DAY, [Order Date], [Ship Date])) AS AvgDeliveryTime
FROM Orders
WHERE [Ship Date] IS NOT NULL AND [Order Date] IS NOT NULL;
```

---

### Orders with the Largest Amount
```sql
SELECT TOP 10
    o.[Order ID],
    SUM(s.Sales) AS TotalOrderSales
FROM Orders o
JOIN Sales s ON o.[Order ID] = s.[Order ID]
GROUP BY o.[Order ID]
ORDER BY TotalOrderSales DESC;
```

---

### Customers Who Made the Most Purchases in Each Region
```sql
SELECT 
    c.Region,
    c.[Customer Name],
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.Region, c.[Customer Name]
ORDER BY c.Region, TotalSales DESC;
```

---

### Total Sales Based on Ship Mode
```sql
SELECT 
    o.[Ship Mode],
    SUM(s.Sales) AS TotalSales
FROM Orders o
JOIN Sales s ON o.[Order ID] = s.[Order ID]
GROUP BY o.[Ship Mode]
ORDER BY TotalSales DESC;
```

---

### Total Sales by Product Subcategory
```sql
SELECT 
    p.[Sub-Category],
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Sub-Category]
ORDER BY TotalSales DESC;
```

---

### Total Sales Based on Product and Customer Categories
```sql
SELECT 
    p.Category,
    c.Segment,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY p.Category, c.Segment
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
