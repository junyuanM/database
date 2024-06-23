use lab2;
DROP FUNCTION IF EXISTS update_balance;

DELIMITER $$

CREATE FUNCTION update_balance(
    account_number INT,
    withdraw_amount DECIMAL(8,2)
) RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    DECLARE result VARCHAR(50);
    
    UPDATE 账户
    SET 余额 = 余额 - withdraw_amount
    WHERE 账户号 = account_number;

    IF ROW_COUNT() = 1 THEN
        SET result = '取款成功';
    ELSE
        SET result = '取款失败';
    END IF;

    RETURN result;
END$$

DELIMITER ;
