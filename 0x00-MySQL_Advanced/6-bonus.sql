DELIMITER $$;
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
) BEGIN
DECLARE project_id INT;
SELECT id INTO project_id
FROM project
WHERE name = project_name;
IF project_id IS NULL THEN
INSERT INTO project (name)
VALUES (project_name);
SET project_id = LAST_INSERT_ID();
END IF;
INSERT INTO correction (user_id, project_id, score)
VALUES (user_id, project_id, score);
END $$ DELIMITER;