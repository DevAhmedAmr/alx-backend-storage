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