SELECT * FROM dbo.Noon;


-- Check the top 10 rated scents that users like from high to low, removing duplicates:
SELECT DISTINCT TOP 10 n.scents, 
                       n.item_rating
FROM dbo.Noon as n

WHERE item_rating >= 5
ORDER BY n.item_rating DESC;

-- Check names and brands of these top 10:
SELECT DISTINCT TOP 10 n.brand,
                       n.name,
                       n.scents, 
                       n.item_rating
FROM dbo.Noon as n

WHERE item_rating >= 5
ORDER BY n.item_rating DESC;


-- Find customers who likes Amber and the name of these products to recommend as well as their rating:
SELECT n.scents,
       n.base_note,
       n.middle_note,
       n.item_rating,
       n.brand,
       n.name
FROM dbo.Noon AS n

WHERE n.base_note IN ('Amber')
    OR n.middle_note IN ('Amber');


-- Fin Avg. rating for each scent
SELECT n.scents, 
       AVG(n.item_rating) as avg_rating
FROM dbo.Noon as n

GROUP BY n.scents
ORDER BY avg_rating DESC;

-- Find Avg. rating for each brand and name
SELECT n.brand,
       n.name,
       AVG(n.item_rating) as avg_rating
FROM dbo.Noon as n 

GROUP BY n.brand, n.name
ORDER BY avg_rating DESC;

-- Top rated scent for each brand
SELECT n.brand, 
       n.scents, 
       MAX(n.item_rating) as max_rating
FROM dbo.Noon as n

GROUP BY n.brand, n.scents
ORDER BY max_rating DESC;



-- Top rated scents >= 5 where we can compare our test for our report at the end to see which ones users like the most:
-- Arabian, Aromatic, Citrus, Floral, Fresh, Fruity, Jasmine, Musk, Oriental