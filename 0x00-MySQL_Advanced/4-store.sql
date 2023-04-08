-- script that creates a trigger
-- trigger decreases quantity of an item afer adding a new order

CREATE TRIGGER decrement
AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;
