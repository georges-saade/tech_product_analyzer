-- CREATE VIEW product_analyzer.review_stats AS(
-- WITH REVIEW_NUMBER AS(
-- SELECT
-- 	products.product_id,
-- 	products.brand,
-- 	products.model,
-- 	reviews.review_date,
-- 	COUNT(CASE WHEN
-- 		reviews.sentiment='Positive' THEN reviews.review_id END) AS positive_reviews,
-- 	COUNT(CASE WHEN
-- 		reviews.sentiment='Negative' THEN reviews.review_id END) AS negative_reviews
-- FROM product_analyzer.fact_reviews as reviews
-- INNER JOIN product_analyzer.dim_product as products
-- ON reviews.product_id=products.product_id
-- GROUP BY
-- 	products.product_id,
-- 	reviews.review_date,
-- 	products.brand,
-- 	products.model,
-- 	products.release_date
-- ORDER BY reviews.review_date
-- 	),

-- REVIEW_PERCENTAGES AS (
--     SELECT
--         product_id,
--         brand,
--         model,
--         review_date,
--         positive_reviews+negative_reviews AS total_reviews,
--         positive_reviews,
--         negative_reviews,
--         ROUND((positive_reviews * 100.0 /NULLIF(positive_reviews+negative_reviews,0)),1) AS positive_percentage,
--         ROUND((negative_reviews * 100.0 /NULLIF(positive_reviews+negative_reviews,0)),1) AS negative_percentage
--     FROM REVIEW_NUMBER
-- 	)
	
-- SELECT
--     product_id,
--     brand,
--     model,
--     review_date,
--     total_reviews,
--     positive_reviews,
--     positive_percentage,
--     negative_reviews,
--     negative_percentage
-- FROM REVIEW_PERCENTAGES
-- ORDER BY review_date
-- )

CREATE VIEW product_analyzer.reviews_stats AS (
    SELECT
    reviews.product_id,
	products.brand,
	products.model,
    reviews.review_date,
    reviews.total_reviews,
    reviews.positive_reviews,
    reviews.positive_percentage,
    reviews.negative_reviews,
    reviews.negative_percentage
FROM product_analyzer.agg_reviews AS reviews
INNER JOIN product_analyzer.dim_product AS products
ON reviews.product_id=products.product_id
)