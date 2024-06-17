DELIMITER $$ CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
) BEGIN
declare project_id INT;
---------------------------------
select id into project_id
from project
where name = project_name;
-------------------------------------
IF project_id is null then
insert into project (name)
values(project_name);
SET project_id = LAST_INSERT_ID();
end if;
---------------------
insert into correction (user_id, project_id, score)
values(user_id, project_id, score);
end $$ DELIMITER;