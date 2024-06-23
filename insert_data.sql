use lab2;
insert into 支行 values('a', 'a支行', 100000);
insert into 支行 values('b', 'b支行', 100000);
insert into 支行 values('c', 'c支行', 100000);

insert into 员工 values('1', '李', '111', '安徽省合肥市蜀山区', '2023-10-01');
insert into 员工 values('2', '郑', '222', '安徽省合肥市蜀山区', '2023-10-01');
insert into 员工 values('4', '王', '337', '安徽省合肥市蜀山区', '2023-10-01');

/*客户*/
insert into 客户 values('456','1','wy','456','zkd','','','','','', '');
insert into 客户 values('123','2','mjy','123','zkd','','','','','', 'C:/Users/Lenovo/Desktop/cnn.png');

insert into 贷款 values(20000.00, 50, NULL, 'a支行', '未借贷', '');
insert into 贷款 values(40000.00, 51, NULL, 'b支行', '未借贷', '');
insert into 贷款 values(60000.00, 52, NULL, 'c支行', '未借贷', '');



insert into 账户 values(001, '2023-10-01', 0,
'美元', 0.03);
insert into 账户 values(002, '2023-10-01', 10000,
'欧元', 0.02);
insert into 账户 values(003, '2023-10-01', 20000,
'人民币', 0.04);

insert into 开户 values('123', 'a支行', 001,
'2023-10-01');
insert into 开户 values('123', 'b支行', 002,
'2023-10-01');
insert into 开户 values('456', 'c支行', 003,
'2023-10-01');


commit;