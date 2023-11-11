-- creates a trigger that updates the items table after every order


DROP TRIGGER IF EXISTS  decrease_quantity_after_order
DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_id = NEW.item_id;
END;

//

DELIMITER ;
