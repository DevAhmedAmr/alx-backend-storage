-- script that creates a trigger that decreases 
--the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
---- @block
CREATE TRIGGER decrease_item
AFTER
INSERT ON orders for each row
UPDATE items
set quantity = quantity - new.number
where name = new.item_name;
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