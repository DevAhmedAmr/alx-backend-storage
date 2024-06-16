-- a SQL script that ranks country origins of bands,
-- ordered by the number of (non - unique) fans
SELECT style,
	formed
FROM metal_bands
WHERE style = "glam rock" -- ORDER BY formed DESC