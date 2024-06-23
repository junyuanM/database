use lab2;
DROP PROCEDURE IF EXISTS input_account_procedure;
DELIMITER $$

CREATE PROCEDURE input_account_procedure(
    IN account_number INT,
    IN withdraw_amount DECIMAL(8,2)
)
BEGIN
    DECLARE current_balance DECIMAL(8,2);
    DECLARE result_message VARCHAR(50);
    
    -- 开始事务
    START TRANSACTION;
    
    -- 获取当前余额
    SELECT 余额 INTO current_balance
    FROM 账户
    WHERE 账户号 = account_number
    FOR UPDATE;
    
    -- 检查是否有足够的余额
    IF current_balance < withdraw_amount THEN
        -- 回滚事务并抛出错误
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '余额不足';
    ELSE
        -- 调用更新余额的函数
        SET result_message = update_balance(account_number, withdraw_amount);
        -- 提交事务
        COMMIT;
    END IF;
    
    -- 返回结果消息
    SELECT result_message AS message;
    
END$$

DELIMITER ;
