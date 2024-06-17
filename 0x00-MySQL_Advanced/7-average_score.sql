-- sql scipt

DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(5, 2);


	SELECT AVG(score)
	into avg_score
	FROM corrections 
	WHERE corrections.user_id = user_id;

	UPDATE users
	set average_score = avg_score
	WHERE corrections.user_id = user_id;

END$$

DELIMITER ;