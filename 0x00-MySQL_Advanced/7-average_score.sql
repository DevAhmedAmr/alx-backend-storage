-- sql scipt

DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id_input INT
)
BEGIN
    DECLARE avg_score DECIMAL(5, 2);


	SELECT AVG(score)
	INTO avg_score
	FROM corrections 
	WHERE corrections.user_id  = user_id_input;

	UPDATE users
	set average_score = avg_score
	WHERE id  = user_id_input;

END$$

DELIMITER ;