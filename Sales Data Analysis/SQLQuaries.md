
# Sales Analysis Report
1. **Revenue trends over time**
2. **Best and worst-performing products**
3. **Regional sales performance**
4. **Customer segmentation insights**

---

## 1. Revenue Trends Over Time

```sql
SELECT 
    YEAR(o.[Order Date]) AS Year,
    MONTH(o.[Order Date]) AS Month,
    SUM(s.Sales) AS MonthlyRevenue
FROM Orders o
JOIN Sales s ON o.[Order ID] = s.[Order ID]
GROUP BY YEAR(o.[Order Date]), MONTH(o.[Order Date])
ORDER BY Year, Month;
```

---

## 2. Best Performing Products

```sql
SELECT TOP 10
    p.[Product Name] AS BestSaleProducts,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY TotalSales DESC;
```

---

## 3. Worst Performing Products

```sql
SELECT TOP 10 
    p.[Product Name] AS WorstSaleProducts,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY TotalSales ASC;
```

---

## 4. Regional Sales Performance

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

## 5. Customer Segmentation Insights

```sql
SELECT 
    c.Segment,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.Segment
ORDER BY TotalSales DESC;
```
