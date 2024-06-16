-- a SQL script that ranks country origins of bands,
-- ordered by the number of (non - unique) fans
-- SELECT origin,
--     count(fans)
-- FROM metal_bands
-- GROUP BY origin
SELECT origin,
    sum(fans) as nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;