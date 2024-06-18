-- SQL script that creates a function SafeDiv that divides 
-- (and returns) the first by the second number or returns 0 
-- if the second number is equal to 0.

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$;
CREATE function SafeDiv( a int ,  b int)
returns float deterministic
BEGIN
	IF b = 0 then
		return 0;
		END IF;

	return a/b;
end $$

DELIMITER ;