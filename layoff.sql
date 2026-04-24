SELECT * FROM core.layoffs;

--Which industry had the most total layoffs overall?--
SELECT industry, SUM(total_laid_off) as total
FROM core.layoffs
GROUP BY industry
ORDER BY total DESC
LIMIT 10;

SELECT 
    EXTRACT(YEAR FROM date) AS year,
    COUNT(*) AS num_events,
    SUM(total_laid_off) AS total_laid_off
FROM core.layoffs
WHERE date IS NOT NULL
GROUP BY year
ORDER BY year;

SELECT 
    stage,
    COUNT(*) AS num_events,
    AVG (percentage_laid_off) AS avg_pct_laid_off
FROM core.layoffs
WHERE stage IS NOT NULL
GROUP BY stage
ORDER BY avg_pct_laid_off DESC;

SELECT company, industry, total_laid_off, date
FROM core.layoffs
WHERE total_laid_off IS NOT NULL
ORDER BY total_laid_off DESC
LIMIT 10;

\copy (SELECT * FROM mart.layoffs_by_industry) TO '/Users/clerancesmal/Desktop/layoffs_by_industry.csv' CSV HEADER;