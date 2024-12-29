# 📊 **Sales Data Analysis with SQL**

## 📜 **Overview**

This project showcases the use of SQL for analyzing sales data, uncovering key trends, and measuring business performance metrics. The analysis aims to derive actionable insights that support data-driven decision-making.

---

## 🛠️ **Key Skills and Tools**

- **SQL**: Aggregations, Joins, Subqueries, Common Table Expressions (CTEs)  
- **Data Analysis**: Revenue trends, top-selling products, regional performance  
- **Database Management**: Handling relational databases with large datasets  
- **Visualization**: Creating actionable charts using Power BI  

---

## 🔑 **Highlights**

- **Comprehensive Analysis**: Covers revenue trends, customer segmentation, and identifying peak sales periods.  
- **KPIs Measured**: Total sales, revenue growth, Average Order Value (AOV), and Customer Lifetime Value (CLV).  
- **Advanced SQL Techniques**:  
  - Window functions for cumulative calculations.  
  - Correlated subqueries for detailed insights.  
  - CTEs for clear and modular SQL queries.  

---

## 🗂️ **Data Description**

### **Data Schema**
- **Customers Table**:  
  - `CustomerID`: Unique identifier for each customer.  
  - `CustomerName`: Name of the customer.  
  - `Region`: Geographic region.  

- **Transactions Table**:  
  - `TransactionID`: Unique transaction identifier.  
  - `Date`: Date of the transaction.  
  - `CustomerID`: Foreign key linking to the Customers table.  
  - `ProductID`: Foreign key linking to the Products table.  
  - `Amount`: Transaction amount.  

- **Products Table**:  
  - `ProductID`: Unique identifier for each product.  
  - `ProductName`: Name of the product.  
  - `Category`: Product category.  

---

## 🧰 **Steps in the Analysis**

### **1. Data Cleaning**
- Handled missing or inconsistent data using SQL functions.  
- Standardized date formats and resolved duplicate entries.  

### **2. Exploratory Data Analysis (EDA)**
- Analyzed revenue distribution across regions.  
- Studied sales performance over time.  
- Identified high-performing products and categories.  

### **3. KPI Calculations**
- Revenue growth rate.  
- Retention rates by customer segments.  
- Average Order Value (AOV).  

### **4. Actionable Insights**
- Pinpointed top-performing regions, products, and seasonal trends.  

---

## 📂 **Repository Contents**

### **1. SQL Scripts**
A collection of SQL queries to analyze the sales data.  

#### **1.1 Total Sales by Region**
```sql
SELECT 
    c.Region,
    SUM(t.Amount) AS TotalSales
FROM Transactions t
JOIN Customers c ON t.CustomerID = c.CustomerID
GROUP BY c.Region
ORDER BY TotalSales DESC;
```

#### **1.2 Monthly Revenue Trends**
```sql
SELECT 
    DATE_FORMAT(t.Date, '%Y-%m') AS Month,
    SUM(t.Amount) AS MonthlyRevenue
FROM Transactions t
GROUP BY Month
ORDER BY Month;
```

#### **1.3 Top-Selling Products**
```sql
SELECT 
    p.ProductName,
    SUM(t.Amount) AS TotalRevenue
FROM Transactions t
JOIN Products p ON t.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalRevenue DESC
LIMIT 5;
```

#### **1.4 Customer Segmentation by Spending**
```sql
SELECT 
    c.CustomerName,
    CASE 
        WHEN SUM(t.Amount) >= 1000 THEN 'High Spender'
        WHEN SUM(t.Amount) >= 500 THEN 'Medium Spender'
        ELSE 'Low Spender'
    END AS SpendingCategory,
    SUM(t.Amount) AS TotalSpent
FROM Transactions t
JOIN Customers c ON t.CustomerID = c.CustomerID
GROUP BY c.CustomerName
ORDER BY TotalSpent DESC;
```

#### **1.5 Least Sold Products**
```sql
SELECT 
    p.ProductName,
    SUM(t.Amount) AS TotalRevenue
FROM Transactions t
JOIN Products p ON t.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalRevenue ASC
LIMIT 5;
```

---

### **2. Data**

#### **2.1 Sample Datasets**
- **customers.csv**  
  ```csv
  CustomerID,CustomerName,Region
  1,John Doe,North
  2,Jane Smith,East
  3,Michael Brown,West
  4,Linda Johnson,South
  5,Emily Davis,North
  ```

- **transactions.csv**  
  ```csv
  TransactionID,Date,CustomerID,ProductID,Amount
  1001,2024-01-15,1,201,150.00
  1002,2024-01-16,2,202,200.00
  1003,2024-01-17,3,203,300.00
  1004,2024-01-18,4,204,250.00
  1005,2024-01-19,5,201,100.00
  ```

- **products.csv**  
  ```csv
  ProductID,ProductName,Category
  201,Laptop,Electronics
  202,Smartphone,Electronics
  203,Desk,Furniture
  204,Chair,Furniture
  ```

---

### **3. Analysis Report**
A PDF report summarizing the key findings:  
- Total revenue and revenue trends over time.  
- Best and worst-performing products.  
- Regional sales performance.  
- Customer segmentation insights.  

---

### **4. Power BI Dashboard**
An interactive Power BI file (`.pbix`) visualizing:  
- **Revenue Trends**: Line chart for monthly revenue.  
- **Top Products**: Bar chart for highest-selling products.  
- **Regional Performance**: Heatmap for revenue distribution by region.  
- **Customer Segmentation**: Pie chart for customer spending categories.  

---

## 🎯 **Business Objectives**
- Identify growth opportunities in underperforming regions.  
- Optimize inventory management for high-demand products.  
- Develop targeted marketing strategies based on customer segmentation.  

---


