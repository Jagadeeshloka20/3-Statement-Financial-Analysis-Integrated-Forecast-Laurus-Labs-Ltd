SELECT fy,revenue,revenue/LAG(revenue) OVER(ORDER BY fy)-1 AS revenue_growth,
ebitda/revenue AS ebitda_margin,pat/revenue AS pat_margin,nwc/revenue AS nwc_intensity
FROM historical_financials ORDER BY fy;
SELECT fy,capex/revenue AS capex_intensity FROM historical_financials ORDER BY fy;
