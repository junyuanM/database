drop database if exists lab2;
create database lab2;
use lab2;

create table 开户 
(
   身份证号                 varchar(20)             not null,
   名字                   varchar(20)             not null,
   账户号                  INTEGER              not null,
   最近访问日期               varchar(20),
   constraint PK_开户 primary key (身份证号, 名字, 账户号)
);


create table 账户 
(
   账户号                  INTEGER              not null,
   开户日期                 varchar(20),
   余额                   DECIMAL(8,2),
   货币类型                 varchar(50),
   利率                   DOUBLE,
   constraint PK_账户 primary key (账户号)
);

create table 员工 
(
   身份证号              varchar(20)             not null,
   姓名                  varchar(50),
   电话号码                varchar(50),
   家庭住址               varchar(50),
   开始工作日期              varchar(20),
   constraint PK_员工 primary key (身份证号)
);


create table 客户 
(
   客户身份证号                 varchar(20)             not null,
   身份证号                varchar(20),
   姓名                   varchar(50),
   联系电话                 varchar(50),
   家庭住址                 varchar(50),
   联系人姓名                varchar(50)                 not null,
   联系人手机号               varchar(50),
   联系人Email           varchar(50),
   联系人与客户关系             varchar(50),
   负责人类型                varchar(50),
   头像地址                  varchar(50),
   constraint PK_客户 primary key (客户身份证号)
);


create table 支行 
(
   城市                   varchar(20)             not null,
   名字                   varchar(20)             not null,
   资产                   DECIMAL(8,2)          not null,
   constraint PK_支行 primary key (名字)
);


create table 贷款 
(
   金额                  DECIMAL(8,2),
   贷款号                  INTEGER              not null,
   账户号                  INTEGER              ,
   名字                   varchar(20),
   贷款状态                   varchar(20),
   还款时间                 varchar(20),
   constraint PK_贷款 primary key (贷款号)
);


alter table 开户
   add constraint FK_开户_客户 foreign key (身份证号)
      references 客户 (客户身份证号);
      

alter table 开户
   add constraint FK_开户2_支行 foreign key (名字)
      references 支行 (名字);
      
alter table 开户
   add constraint FK_开户3_账户 foreign key (账户号)
      references 账户 (账户号);

alter table 客户
   add constraint FK_客户_负责_员工 foreign key (身份证号)
      references 员工 (身份证号);

alter table 贷款
   add constraint FK_贷款_拥有贷款_支行 foreign key (名字)
      references 支行 (名字);
      
alter table 贷款
   add constraint FK_贷款_拥有贷款_账户 foreign key (账户号)
      references 账户 (账户号);
