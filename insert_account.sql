use lab2;
DROP PROCEDURE IF EXISTS insert_account_procedure;
DELIMITER $$

CREATE PROCEDURE insert_account_procedure(
    IN p_account_number INTEGER,
    IN p_branch_name VARCHAR(20),
    IN p_account_holder_id VARCHAR(20),
    IN p_balance DECIMAL(8,2),
    IN p_interest_rate DOUBLE,
    IN p_currency_type VARCHAR(50),
    IN p_account_type VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '操作失败: 存储过程中出现异常';
    END;

    START TRANSACTION;

    IF p_account_type = '账户' THEN
        IF NOT EXISTS (SELECT * FROM 账户 WHERE 账户号 = p_account_number) THEN
            INSERT INTO 账户 (账户号, 余额, 利率, 货币类型)
            VALUES (p_account_number, p_balance, p_interest_rate, p_currency_type);
        END IF;

        INSERT INTO 开户 (身份证号, 名字, 账户号, 最近访问日期)
        VALUES (p_account_holder_id, p_branch_name, p_account_number, NULL);
    END IF;

    COMMIT;
END$$

DELIMITER ;
