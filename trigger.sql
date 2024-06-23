use lab2;

-- Drop existing triggers if they exist
DROP TRIGGER IF EXISTS set_open_date_savings;
DELIMITER $$
-- Create trigger for 账户 table
CREATE TRIGGER set_open_date_savings
BEFORE INSERT ON 账户
FOR EACH ROW
BEGIN
    SET NEW.开户日期 = CURRENT_DATE();
END$$
DELIMITER ;
