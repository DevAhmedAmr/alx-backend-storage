DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting  as
SELECT *
FROM students
WHERE (score < 80) AND (last_meeting is NULL 
	OR DATEDIFF(CURDATE(), last_meeting) <= 30);