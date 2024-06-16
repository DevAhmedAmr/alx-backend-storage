-- script that creates a trigger that decreases 
--the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
---- @block
CREATE TRIGGER decrease_item
AFTER
INSERT ON orders FOR EACH ROW BEGIN
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
END;
-- -- @block
-- DROP TRIGGER decrease_item;
-- ---
-- ---
-- ---
-- --
-- -- @block
-- INSERT INTO orders (item_name, number)
-- VALUES ('apple', 1);
-- INSERT INTO orders (item_name, number)
-- VALUES ('apple', 3);
-- INSERT INTO orders (item_name, number)
-- VALUES ('pear', 2);
-- --
-- --
-- --
-- --
-- -- @block
-- SELECT *
-- FROM items;
-- SELECT *
-- FROM orders;