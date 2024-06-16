-- @block
CREATE TRIGGER reset_valid_email before
UPDATE on users for each row if (new.email != old.email) then
SET new.valid_email = 0;
END IF;