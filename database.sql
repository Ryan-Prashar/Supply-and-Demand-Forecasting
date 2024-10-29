-- Create demand table
CREATE TABLE historical_demand (
    date DATE,
    product_id INT,
    quantity INT
);

-- Create supply table
CREATE TABLE historical_supply (
    date DATE,
    product_id INT,
    quantity INT
);

-- Sample data for demand
INSERT INTO historical_demand (date, product_id, quantity)
VALUES
    ('2023-01-01', 1, 150),
    ('2023-01-02', 1, 200),
    ('2023-01-03', 1, 180),
    ('2023-01-01', 2, 300),
    ('2023-01-02', 2, 320);

-- Sample data for supply
INSERT INTO historical_supply (date, product_id, quantity)
VALUES
    ('2023-01-01', 1, 140),
    ('2023-01-02', 1, 210),
    ('2023-01-03', 1, 170),
    ('2023-01-01', 2, 310),
    ('2023-01-02', 2, 300);


-- Calculate daily average demand
SELECT date, AVG(quantity) AS avg_demand
FROM historical_demand
GROUP BY date
ORDER BY date;

-- Calculate daily average supply
SELECT date, AVG(quantity) AS avg_supply
FROM historical_supply
GROUP BY date
ORDER BY date;


-- Monthly demand pattern
SELECT MONTH(date) AS month, AVG(quantity) AS avg_monthly_demand
FROM historical_demand
GROUP BY month
ORDER BY month;
