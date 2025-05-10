/* report summarizing key findings:

    Revenue trends over time
    Best and worst-performing products
    Regional sales performance
    Customer segmentation insights
*/

--Revenue trends over time
SELECT 
    YEAR(o.[Order Date]) AS Year,
    MONTH(o.[Order Date]) AS Month,
    SUM(s.Sales) AS MonthlyRevenue
FROM Orders o
JOIN Sales s ON o.[Order ID] = s.[Order ID]
GROUP BY YEAR(o.[Order Date]), MONTH(o.[Order Date])
ORDER BY Year, Month;

--Best performing products
SELECT top 10
    p.[Product Name] AS BestSaleProducts,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY TotalSales DESC;

--worst performing products
SELECT top 10 
    p.[Product Name] AS WorstSaleProducts,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Products p ON s.[Product ID] = p.[Product ID]
GROUP BY p.[Product Name]
ORDER BY TotalSales Asc;

--    Regional sales performance
SELECT
    c.Region,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.Region
ORDER BY TotalSales DESC;

--    Customer segmentation insights
SELECT 
    c.Segment,
    SUM(s.Sales) AS TotalSales
FROM Sales s
JOIN Customers c ON s.[Customer ID] = c.[Customer ID]
GROUP BY c.Segment
ORDER BY TotalSales DESC;
