from ui import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate, QTime, Qt
from PyQt5 import QtCore
import sys
import mysql.connector
import decimal
import re  # 添加正则表达式模块

def to_date(string):
    date = str(string).split('-')
    return date[0] + '/' + date[1] + '/' + date[2][0:2]

def equal(left, right, String=True):
    if right == '' and left != '头像地址':
        return 'True'
    else:
        return left + ' = ' + to_str(right, String)

def to_str(value, String=True):
    if String:
        return '\'' + value + '\''
    else:
        return value
    
def digit_number(value):
    return re.fullmatch(r'\d{3}', value) is not None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('银行业务系统')
        self.bind_up()
        self.query = ""
        self.file_path = ''
        self.op = [' = ', ' != ', ' > ', ' < ']
        self.customer = ()

    def bind_up(self):
        self.button_add_customer.clicked.connect(self.insert_custom)
        self.button_delete_customer.clicked.connect(self.delete_custom)
        self.button_update_customer.clicked.connect(self.update_custom)
        self.button_query_customer.clicked.connect(self.select_custom)
        self.button_clear_customer.clicked.connect(self.clear_custom)
        self.button_avatar.clicked.connect(self.upload_avatar)

        self.button_open_account.clicked.connect(self.insert_account)
        self.button_close_account.clicked.connect(self.delete_account)
        self.button_deposit.clicked.connect(self.deposit_account)
        self.button_withdraw.clicked.connect(self.withdraw_account)
        self.button_query_account.clicked.connect(self.select_account)
        self.button_clear_account.clicked.connect(self.clear_account)

        self.button_add_loan.clicked.connect(self.insert_loan)
        self.button_delete_loan.clicked.connect(self.delete_loan)
        self.button_query_loan.clicked.connect(self.select_loan)
        self.button_clear_loan.clicked.connect(self.clear_loan)
        self.button_issue_loan.clicked.connect(self.pay_loan)

        self.button_query_employees.clicked.connect(self.select_employee)

    def execute(self, receive):
        global db
        result = []
        try:
            cursor = db.cursor()
            cursor.execute(self.query)
            if receive:
                result = cursor.fetchall()
            else:
                result = True
            db.commit()
            cursor.close()
        except mysql.connector.Error as err:
            self.error_input(f'SQL执行失败: {err}')
            return False
        self.last = ''
        return result

    def error_input(self, err_msg):
        QMessageBox.information(self, "错误提示", err_msg, QMessageBox.Yes | QMessageBox.No)

    # Customer management
    def upload_avatar(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, '选择头像', '', 'Images (*.png *.jpg *.jpeg)')
        if self.file_path:
            self.label_avatar.setPixmap(QPixmap(self.file_path).scaled(self.label_avatar.size(), QtCore.Qt.KeepAspectRatio))

    def insert_custom(self):
        if not digit_number(self.lineEdit_customer_id.text()) or not digit_number(self.lineEdit_phone.text()):
            self.error_input('身份证号和电话号码必须是3位数字')
            return
        print("file_path,", self.file_path)
        if self.lineEdit_customer_id.text() == '' or self.lineEdit_id_number.text() == '' or self.lineEdit_name.text() == '':
            self.error_input('输入信息不足!')
            return
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.query = 'insert into 客户(客户身份证号, 身份证号, 姓名, 联系电话, 家庭住址, 联系人姓名, 联系人手机号, 联系人Email, 联系人与客户关系, 负责人类型, 头像地址) Values(' + to_str(self.lineEdit_customer_id.text()) + ', ' + to_str(self.lineEdit_id_number.text()) + ', ' + to_str(self.lineEdit_name.text()) + ', ' + to_str(self.lineEdit_phone.text()) + ', ' + to_str(self.lineEdit_address.text()) + ', ' + to_str(self.lineEdit_contact_name.text()) + ', ' + to_str(self.lineEdit_contact_phone.text()) + ', ' + to_str(self.lineEdit_contact_email.text()) + ', ' + to_str(self.lineEdit_contact_relation.text()) + ',' + to_str('账户负责人') + ',' + to_str(self.file_path) + ')'
        self.execute(False)

    def delete_custom(self):
        self.select_custom()
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.query = 'delete from 客户 where ' + equal('客户身份证号', self.lineEdit_customer_id.text()) + ' and ' + equal('身份证号', self.lineEdit_id_number.text()) + ' and ' + equal('姓名', self.lineEdit_name.text()) + ' and ' + equal('联系电话 ', self.lineEdit_phone.text()) + ' and ' + equal('家庭住址', self.lineEdit_address.text()) + ' and ' + equal('联系人姓名', self.lineEdit_contact_name.text()) + ' and ' + equal('联系人手机号', self.lineEdit_contact_phone.text()) + ' and ' + equal('联系人Email', self.lineEdit_contact_email.text()) + ' and ' + equal('联系人与客户关系', self.lineEdit_contact_relation.text())
        if self.execute(False):
            self.file_path = ''
            self.label_avatar.setPixmap(QPixmap(self.file_path).scaled(self.label_avatar.size(), QtCore.Qt.KeepAspectRatio))
        else:
            self.error_input('具体原因：客户存在着关联账户或者贷款记录!')
        self.tree_widget_customers.clear()


    def update_custom(self):
        if not digit_number(self.lineEdit_customer_id.text()) or not digit_number(self.lineEdit_phone.text()):
            self.error_input('身份证号和电话号码必须是3位数字')
            return
        if self.lineEdit_customer_id.text() == '' or self.lineEdit_id_number.text() == '' or self.lineEdit_contact_name.text() == '' or self.lineEdit_name.text() == '':
            self.error_input('关键信息缺失!')
            return
        if self.lineEdit_phone.text() == '' or self.lineEdit_address.text() == '' or self.lineEdit_phone.text() == '' or self.lineEdit_contact_phone.text() == '' or self.lineEdit_contact_email.text() == '' or self.lineEdit_contact_relation.text() == '':
            self.error_input('更新时请补全信息，没有则填 无 ')
            return

        setting = equal('身份证号', self.lineEdit_id_number.text()) + ', ' + equal('姓名', self.lineEdit_name.text()) + ', ' + equal('联系电话 ', self.lineEdit_phone.text(), True) + ', ' + equal('家庭住址', self.lineEdit_address.text()) + ', ' + equal('联系人姓名', self.lineEdit_contact_name.text()) + ', ' + equal('联系人手机号', self.lineEdit_contact_phone.text()) + ', ' + equal('联系人Email', self.lineEdit_contact_email.text()) + ', ' + equal('联系人与客户关系', self.lineEdit_contact_relation.text()) + ', ' + equal('头像地址', self.file_path)
        # setting = equal('客户身份证号', self.lineEdit_customer_id.text()) + ', ' + equal('身份证号', self.lineEdit_id_number.text()) + ', ' + equal('姓名', self.lineEdit_name.text()) + ', ' + equal('联系电话 ', self.lineEdit_phone.text(), True) + ', ' + equal('家庭住址', self.lineEdit_address.text()) + ', ' + equal('联系人姓名', self.lineEdit_contact_name.text()) + ', ' + equal('联系人手机号', self.lineEdit_contact_phone.text()) + ', ' + equal('联系人Email', self.lineEdit_contact_email.text()) + ', ' + equal('联系人与客户关系', self.lineEdit_contact_relation.text()) + ', ' + equal('头像地址', self.file_path)
        where_customer = equal('客户身份证号', self.customer[0])
        self.query = 'update 客户 set ' + setting + ' where ' + where_customer
        print("query,", self.query)
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.execute(False)

    def select_custom(self):
        self.query = 'select * from 客户 where ' + equal('客户身份证号', self.lineEdit_customer_id.text()) + ' and ' + equal('身份证号', self.lineEdit_id_number.text()) + ' and ' + equal('姓名', self.lineEdit_name.text()) + ' and ' + equal('联系电话 ', self.lineEdit_phone.text()) + ' and ' + equal('家庭住址', self.lineEdit_address.text()) + ' and ' + equal('联系人姓名', self.lineEdit_contact_name.text()) + ' and ' + equal('联系人手机号', self.lineEdit_contact_phone.text()) + ' and ' + equal('联系人Email', self.lineEdit_contact_email.text()) + ' and ' + equal('联系人与客户关系', self.lineEdit_contact_relation.text())
        query_result = self.execute(True)
        if status == 0 and query_result is not None:
            if len(query_result) == 1:
                self.customer = query_result[0]
                self.file_path = query_result[0][-1]
                print("file:", self.file_path)
                if self.file_path:
                    self.label_avatar.setPixmap(QPixmap(self.file_path).scaled(self.label_avatar.size(), QtCore.Qt.KeepAspectRatio))
                self.show_client(query_result)  
            else:
                self.file_path = ''
                print("file:", self.file_path)
                if self.file_path:
                    self.label_avatar.setPixmap(QPixmap(self.file_path).scaled(self.label_avatar.size(), QtCore.Qt.KeepAspectRatio))
                self.show_client(query_result)  

    def clear_custom(self):
        self.lineEdit_customer_id.setText('')
        self.lineEdit_id_number.setText('')
        self.lineEdit_name.setText('')
        self.lineEdit_phone.setText('')
        self.lineEdit_address.setText('')
        self.lineEdit_contact_name.setText('')
        self.lineEdit_contact_phone.setText('')
        self.lineEdit_contact_email.setText('')
        self.lineEdit_contact_relation.setText('')
        self.file_path = ''
        self.label_avatar.setPixmap(QPixmap(self.file_path).scaled(self.label_avatar.size(), QtCore.Qt.KeepAspectRatio))

    def show_client(self, result):
        self.tree_widget_customers.clear()
        L = []
        for row in result:
            L.append(QTreeWidgetItem([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9])]))
        self.tree_widget_customers.addTopLevelItems(L)

    def insert_account(self):
        if self.lineEdit_account_number.text() == '' or self.lineEdit_branch_name.text() == '' or self.lineEdit_account_holder_id.text() == '' or self.lineEdit_balance.text() == '':
            self.error_input('输入信息不足!')
            return
        # self.combo_box_comparison.setCurrentIndex(0)
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        account_type = '账户' 
        interest_rate = self.lineEdit_interest_rate.text() 
        currency_type = self.lineEdit_currency_type.text() 

        if account_type == '账户' and (interest_rate == '' or currency_type == ''):
            self.error_input('请填写货币类型和利率！')
            return

        try:
            cursor = db.cursor()
            cursor.callproc('insert_account_procedure', [
				self.lineEdit_account_number.text(),
				self.lineEdit_branch_name.text(),
				self.lineEdit_account_holder_id.text(),
				self.lineEdit_balance.text(),
				interest_rate,
				currency_type,
				account_type
			])
            db.commit()
            cursor.close()
            self.error_input('账户插入成功')
        except mysql.connector.Error as err:
            self.error_input(f'SQL执行失败: {err}')


    def delete_account(self):
        if self.lineEdit_account_number.text() == '':
            self.error_input('请给定销户账号！')
            return
        self.select_account()
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        if self.lineEdit_balance.text() == '':
            money = 'True'
        else:
            money = '余额' + '=' + self.lineEdit_balance.text()

        self.query = 'delete from 开户 where ' + equal('账户号', self.lineEdit_account_number.text(), False)
        self.execute(False)
        self.query = 'delete from 账户 where ' + equal('账户号', self.lineEdit_account_number.text(), False) + ' and ' + equal('开户日期', self.lineEdit_time.text()) + ' and ' + money + ' and ' + equal('利率', self.lineEdit_interest_rate.text(), False) + ' and ' + equal('货币类型', self.lineEdit_currency_type.text())

        self.execute(False)

    def select_account(self):
        if self.lineEdit_balance.text() == '':
            money = 'True'
        else:
            money = '余额' + '=' + self.lineEdit_balance.text()
        self.query = 'select 账户.账户号 as 账户号, 开户日期, 余额, 利率, 货币类型, 开户.名字 as 开户行, 身份证号 from 账户, 开户 where 账户.账户号 = 开户.账户号 and ' + equal('账户.账户号', self.lineEdit_account_number.text(), False) + ' and ' + equal('开户日期', self.lineEdit_time.text()) + ' and ' + money + ' and ' + equal('利率', self.lineEdit_interest_rate.text(), False) + ' and ' + equal('货币类型', self.lineEdit_currency_type.text()) + ' and ' + equal('名字', self.lineEdit_branch_name.text()) + ' and ' + equal('身份证号', self.lineEdit_account_holder_id.text())
        query_result = self.execute(True)
        if status == 0 and query_result is not None:
            self.show_account(query_result)

    def clear_account(self):
        self.lineEdit_account_number.setText('')
        self.lineEdit_time.setText('')
        self.lineEdit_balance.setText('')
        self.lineEdit_interest_rate.setText('')
        self.lineEdit_currency_type.setText('')
        self.lineEdit_branch_name.setText('')
        self.lineEdit_account_holder_id.setText('')
        self.lineEdit_input_amount.setText('')

    def show_account(self, result):
        _translate = QtCore.QCoreApplication.translate
        self.tree_widget_accounts.clear()
        L = []
        self.tree_widget_accounts.headerItem().setText(0, _translate("MainWindow", "账户号"))
        self.tree_widget_accounts.headerItem().setText(1, _translate("MainWindow", "开户支行"))
        self.tree_widget_accounts.headerItem().setText(2, _translate("MainWindow", "身份证号"))
        self.tree_widget_accounts.headerItem().setText(3, _translate("MainWindow", "开户日期"))
        self.tree_widget_accounts.headerItem().setText(4, _translate("MainWindow", "余额"))
        self.tree_widget_accounts.headerItem().setText(5, _translate("MainWindow", "利率"))
        self.tree_widget_accounts.headerItem().setText(6, _translate("MainWindow", "货币类型"))
        for row in result:
            date = to_date(row[1])
            L.append(QTreeWidgetItem([str(row[0]), str(row[5]), str(row[6]), date, str(row[2]), str(row[3]), str(row[4])]))
        self.tree_widget_accounts.addTopLevelItems(L)

    def deposit_account(self):
        # 实现存款功能
        if self.lineEdit_account_number.text() == '':
            self.error_input('请给定存款账号！')
            return
        self.select_account()
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.query = 'select * from 账户 where ' + equal('账户号', self.lineEdit_account_number.text())
        query_result = self.execute(True)
        print("账户， ", query_result)
        self.query = 'update 账户 set ' + equal('余额', str(decimal.Decimal(self.lineEdit_input_amount.text()) + query_result[0][2])) + ' where ' + equal('账户号', self.lineEdit_account_number.text()) 
        if self.execute(False):
            print("存款成功")
        else:
            self.error_input('存款失败!')
        

    def withdraw_account(self):
        # 实现取款功能
        if self.lineEdit_account_number.text() == '':
            self.error_input('请给定取款账号！')
            return
        self.select_account()
        try:
            cursor = db.cursor()
            cursor.callproc('input_account_procedure', [
				self.lineEdit_account_number.text(),
				self.lineEdit_input_amount.text()
			])
            db.commit()
            cursor.close()
            self.error_input('取钱成功')
        except mysql.connector.Error as err:
            self.error_input(f'SQL执行失败: {err}')

    # Loan management
    def insert_loan(self):
        if self.lineEdit_repayment_plan.text() == '' or self.lineEdit_borrower_id.text() == '' or self.lineEdit_loan_id.text() == '':
            self.error_input('输入信息不足!')
            return
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.query = 'select 金额 from 贷款 where 贷款号 = ' + self.lineEdit_loan_id.text()
        result = self.execute(True)
        money = result[0][0]
        print("money", money)
        self.query = 'update 贷款 set ' + equal('账户号', self.lineEdit_borrower_id.text()) + ', ' + equal('贷款状态', '已借贷') + ', ' + equal('还款时间', self.lineEdit_repayment_plan.text()) + ' where ' + equal('贷款号', self.lineEdit_loan_id.text()) 
        self.execute(False)
        self.query = 'select * from 账户 where ' + equal('账户号', self.lineEdit_borrower_id.text())
        query_result = self.execute(True)
        print("账户， ", query_result)
        self.query = 'update 账户 set ' + equal('余额', str(money + query_result[0][2])) + ' where ' + equal('账户号', self.lineEdit_borrower_id.text()) 
        self.execute(False)
        self.select_loan()
        

    def delete_loan(self):
        self.select_loan()
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.query = 'select 金额 from 贷款 where 贷款号 = ' + self.lineEdit_loan_id.text()
        result = self.execute(True)
        money = result[0][0]
        self.query = 'select * from 账户 where ' + equal('账户号', self.lineEdit_borrower_id.text())
        query_result = self.execute(True)
        print("账户， ", query_result)
        if money > query_result[0][2]:
            self.error_input('金额不足!')
        else:
            self.query = 'update 账户 set ' + equal('余额', str(query_result[0][2] - money)) + ' where ' + equal('账户号', self.lineEdit_borrower_id.text()) 
            self.execute(False)
            self.query = 'update 贷款 set ' + equal('贷款状态', '已还款') + ' where ' + equal('贷款号', self.lineEdit_loan_id.text()) 
            self.execute(False)
            self.select_loan()

    def select_loan(self):
        self.query = 'select * from 贷款 where ' + equal('金额', self.lineEdit_loan_amount.text(), False)  + ' and ' + equal('贷款号', self.lineEdit_loan_id.text(), False) + ' and ' + equal('名字', self.lineEdit_branch.text(), True)
        query_result = self.execute(True)
        if status == 0 and query_result is not None:
            self.show_loan(query_result)

    def clear_loan(self):
        self.lineEdit_loan_amount.setText('')
        self.lineEdit_loan_id.setText('')
        self.lineEdit_borrower_id.setText('')
        self.lineEdit_branch.setText('')
        self.lineEdit_repayment_plan.setText('')

    def show_loan(self, result):
        self.tree_widget_loans.clear()
        self.tree_widget_loans.setColumnCount(5)
        self.tree_widget_loans.setHeaderLabels(["贷款金额", "贷款号", "借贷账户", "支行名称", "贷款状态"])
        for row in result:
            amount = str(row[0])
            loan_id = str(row[1])
            account_id = str(row[2])
            branch_name = str(row[3])
            status = str(row[4])
            item = QTreeWidgetItem([
                amount,
                loan_id,
                account_id,
                branch_name,
                status
            ])
            self.tree_widget_loans.addTopLevelItem(item)

    def pay_loan(self):
        if self.lineEdit_loan_id.text() == '' or self.lineEdit_loan_amount.text() == '' or self.lineEdit_branch.text() == '':
            self.error_input('输入发放贷款信息不足！')
            return
        # print("sssssssssssss", self.lineEdit_loan_amount.text())
        self.query = 'insert into 贷款(金额, 贷款号, 名字, 贷款状态) Values(' + to_str(self.lineEdit_loan_amount.text()) + ', ' + to_str(self.lineEdit_loan_id.text()) + ', ' + to_str(self.lineEdit_branch.text()) + ', ' + to_str('未借贷') + ')'
        reply = QMessageBox.question(self, '确认', "确定执行操作?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.execute(False)
        self.select_loan()

    # Employee management
    def select_employee(self):
        self.query = 'select * from 员工'
        query_result = self.execute(True)
        if status == 0 and query_result is not None:
            self.show_employees(query_result)

    def show_employees(self, result):
        self.tree_widget_employees.clear()
        self.tree_widget_employees.setColumnCount(5)
        self.tree_widget_employees.setHeaderLabels(["身份证号", "姓名", "电话号码", "家庭住址", "开始工作日期"])
        for row in result:
            item = QTreeWidgetItem([
                str(row[0]),  # 身份证号
                str(row[1]),  # 姓名
                str(row[2]),  # 电话号码
                str(row[3]),  # 家庭住址
                str(row[4])   # 开始工作日期
            ])
            self.tree_widget_employees.addTopLevelItem(item)

if __name__ == "__main__":
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",  # 确保主机地址与 Workbench 中的一致
            user="root",
            password="Mjy1300911259",  # 请替换为实际的密码
            database="lab2",  # 修改为你的数据库名称
            charset="utf8"
        )
        print("Connected successfully!")
        status = 0
    except mysql.connector.Error as err:
        status = 1
        print(f"Failed to connect to the database: {err}")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

    if status == 0:
        db.close()
