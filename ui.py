from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 1150, 750))
        self.tabWidget.setFont(QtGui.QFont("Arial", 12))
        self.tabWidget.setStyleSheet("background:rgb(220, 220, 220); border-radius:10px;")
        self.tabWidget.setObjectName("tabWidget")
        
        # 客户管理模块
        self.tab_customer_management = QtWidgets.QWidget()
        self.tab_customer_management.setObjectName("tab_customer_management")
        self.widget_9 = QtWidgets.QWidget(self.tab_customer_management)
        self.widget_9.setGeometry(QtCore.QRect(10, 0, 1130, 730))
        self.widget_9.setStyleSheet("background:rgb(250, 250, 250); border: 1px solid gray;")
        self.widget_9.setObjectName("widget_9")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setGeometry(QtCore.QRect(10, 220, 1110, 500))
        self.widget_10.setObjectName("widget_10")
        self.tree_widget_customers = QtWidgets.QTreeWidget(self.widget_10)
        self.tree_widget_customers.setGeometry(QtCore.QRect(10, 10, 1080, 351))
        self.tree_widget_customers.setFont(QtGui.QFont("Arial", 12))
        self.tree_widget_customers.setStyleSheet("border: 1px solid rgb(100, 100, 100); border-radius: 5px;")
        self.tree_widget_customers.setObjectName("tree_widget_customers")
        self.label_manager_id = QtWidgets.QLabel(self.widget_9)
        self.label_manager_id.setGeometry(QtCore.QRect(540, 20, 141, 41))
        self.label_manager_id.setFont(QtGui.QFont("Arial", 12))
        self.label_manager_id.setObjectName("label_manager_id")
        self.lineEdit_id_number = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_id_number.setGeometry(QtCore.QRect(680, 30, 161, 31))
        self.lineEdit_id_number.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_id_number.setObjectName("lineEdit_id_number")
        self.label_customer_id = QtWidgets.QLabel(self.widget_9)
        self.label_customer_id.setGeometry(QtCore.QRect(20, 10, 91, 41))
        self.label_customer_id.setFont(QtGui.QFont("Arial", 12))
        self.label_customer_id.setObjectName("label_customer_id")
        self.lineEdit_customer_id = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_customer_id.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.lineEdit_customer_id.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_customer_id.setObjectName("lineEdit_customer_id")
        self.label_name = QtWidgets.QLabel(self.widget_9)
        self.label_name.setGeometry(QtCore.QRect(30, 60, 81, 41))
        self.label_name.setFont(QtGui.QFont("Arial", 12))
        self.label_name.setObjectName("label_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_name.setGeometry(QtCore.QRect(120, 70, 131, 31))
        self.lineEdit_name.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_phone = QtWidgets.QLabel(self.widget_9)
        self.label_phone.setGeometry(QtCore.QRect(20, 110, 91, 41))
        self.label_phone.setFont(QtGui.QFont("Arial", 12))
        self.label_phone.setObjectName("label_phone")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_phone.setGeometry(QtCore.QRect(130, 120, 181, 31))
        self.lineEdit_phone.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.label_address = QtWidgets.QLabel(self.widget_9)
        self.label_address.setGeometry(QtCore.QRect(320, 110, 91, 41))
        self.label_address.setFont(QtGui.QFont("Arial", 12))
        self.label_address.setObjectName("label_address")
        self.lineEdit_address = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_address.setGeometry(QtCore.QRect(430, 120, 411, 31))
        self.lineEdit_address.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.label_contact_name = QtWidgets.QLabel(self.widget_9)
        self.label_contact_name.setGeometry(QtCore.QRect(290, 20, 121, 41))
        self.label_contact_name.setFont(QtGui.QFont("Arial", 12))
        self.label_contact_name.setObjectName("label_contact_name")
        self.lineEdit_contact_name = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_contact_name.setGeometry(QtCore.QRect(400, 30, 121, 31))
        self.lineEdit_contact_name.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_contact_name.setObjectName("lineEdit_contact_name")
        self.label_contact_phone = QtWidgets.QLabel(self.widget_9)
        self.label_contact_phone.setGeometry(QtCore.QRect(10, 160, 131, 41))
        self.label_contact_phone.setFont(QtGui.QFont("Arial", 12))
        self.label_contact_phone.setObjectName("label_contact_phone")
        self.lineEdit_contact_phone = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_contact_phone.setGeometry(QtCore.QRect(130, 170, 221, 31))
        self.lineEdit_contact_phone.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_contact_phone.setObjectName("lineEdit_contact_phone")
        self.label_contact_email = QtWidgets.QLabel(self.widget_9)
        self.label_contact_email.setGeometry(QtCore.QRect(270, 70, 121, 41))
        self.label_contact_email.setFont(QtGui.QFont("Arial", 12))
        self.label_contact_email.setObjectName("label_contact_email")
        self.lineEdit_contact_email = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_contact_email.setGeometry(QtCore.QRect(400, 80, 181, 31))
        self.lineEdit_contact_email.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_contact_email.setObjectName("lineEdit_contact_email")
        self.label_contact_relation = QtWidgets.QLabel(self.widget_9)
        self.label_contact_relation.setGeometry(QtCore.QRect(590, 70, 121, 41))
        self.label_contact_relation.setFont(QtGui.QFont("Arial", 12))
        self.label_contact_relation.setObjectName("label_contact_relation")
        self.lineEdit_contact_relation = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_contact_relation.setGeometry(QtCore.QRect(710, 70, 131, 31))
        self.lineEdit_contact_relation.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_contact_relation.setObjectName("lineEdit_contact_relation")
        self.button_add_customer = QtWidgets.QPushButton(self.widget_9)
        self.button_add_customer.setGeometry(QtCore.QRect(370, 160, 91, 61))
        self.button_add_customer.setFont(QtGui.QFont("Arial", 15))
        self.button_add_customer.setStyleSheet("QPushButton {background-color:rgb(0, 170, 0); color: white; border-radius: 10px;}")
        self.button_add_customer.setObjectName("button_add_customer")
        self.button_delete_customer = QtWidgets.QPushButton(self.widget_9)
        self.button_delete_customer.setGeometry(QtCore.QRect(470, 160, 81, 61))
        self.button_delete_customer.setFont(QtGui.QFont("Arial", 15))
        self.button_delete_customer.setStyleSheet("QPushButton {background-color:rgb(255, 0, 0); color: white; border-radius: 10px;}")
        self.button_delete_customer.setObjectName("button_delete_customer")
        self.button_update_customer = QtWidgets.QPushButton(self.widget_9)
        self.button_update_customer.setGeometry(QtCore.QRect(560, 160, 91, 61))
        self.button_update_customer.setFont(QtGui.QFont("Arial", 15))
        self.button_update_customer.setStyleSheet("QPushButton {background-color:rgb(0, 0, 255); color: white; border-radius: 10px;}")
        self.button_update_customer.setObjectName("button_update_customer")
        self.button_query_customer = QtWidgets.QPushButton(self.widget_9)
        self.button_query_customer.setGeometry(QtCore.QRect(660, 160, 91, 61))
        self.button_query_customer.setFont(QtGui.QFont("Arial", 15))
        self.button_query_customer.setStyleSheet("QPushButton {background-color:rgb(0, 170, 255); color: white; border-radius: 10px;}")
        self.button_query_customer.setObjectName("button_query_customer")
        self.button_clear_customer = QtWidgets.QPushButton(self.widget_9)
        self.button_clear_customer.setGeometry(QtCore.QRect(760, 160, 81, 61))
        self.button_clear_customer.setFont(QtGui.QFont("Arial", 13))
        self.button_clear_customer.setStyleSheet("QPushButton {background-color: rgb(170, 170, 170); color: white; border-radius: 10px;}")
        self.button_clear_customer.setObjectName("button_clear_customer")
        self.button_avatar = QtWidgets.QPushButton(self.widget_9)
        self.button_avatar.setGeometry(QtCore.QRect(850, 160, 91, 61))
        self.button_avatar.setFont(QtGui.QFont("Arial", 15))
        self.button_avatar.setStyleSheet("QPushButton {background-color: rgb(255, 170, 0); color: white; border-radius: 10px;}")
        self.button_avatar.setObjectName("button_avatar")
        self.label_avatar = QtWidgets.QLabel(self.widget_9)
        self.label_avatar.setGeometry(QtCore.QRect(850, 20, 141, 141))
        self.label_avatar.setObjectName("label_avatar")
        self.tabWidget.addTab(self.tab_customer_management, "")

        # 员工管理模块
        self.tab_employee_management = QtWidgets.QWidget()
        self.tab_employee_management.setObjectName("tab_employee_management")
        self.widget_employee = QtWidgets.QWidget(self.tab_employee_management)
        self.widget_employee.setGeometry(QtCore.QRect(10, 0, 1130, 730))
        self.widget_employee.setStyleSheet("background:rgb(250, 250, 250); border: 1px solid gray;")
        self.widget_employee.setObjectName("widget_employee")
        self.tree_widget_employees = QtWidgets.QTreeWidget(self.widget_employee)
        self.tree_widget_employees.setGeometry(QtCore.QRect(10, 10, 1080, 351))
        self.tree_widget_employees.setFont(QtGui.QFont("Arial", 12))
        self.tree_widget_employees.setStyleSheet("border: 1px solid rgb(100, 100, 100); border-radius: 5px;")
        self.tree_widget_employees.setObjectName("tree_widget_employees")
        self.button_query_employees = QtWidgets.QPushButton(self.widget_employee)
        self.button_query_employees.setGeometry(QtCore.QRect(460, 380, 161, 61))
        self.button_query_employees.setFont(QtGui.QFont("Arial", 15))
        self.button_query_employees.setStyleSheet("QPushButton {background-color: rgb(0, 170, 255); color: white; border-radius: 10px;}")
        self.button_query_employees.setObjectName("button_query_employees")
        self.tabWidget.addTab(self.tab_employee_management, "")

        # 账户管理模块
        self.tab_account_management = QtWidgets.QWidget()
        self.tab_account_management.setObjectName("tab_account_management")
        self.widget_13 = QtWidgets.QWidget(self.tab_account_management)
        self.widget_13.setGeometry(QtCore.QRect(10, 0, 1130, 730))
        self.widget_13.setStyleSheet("background:rgb(250, 250, 250); border: 1px solid gray;")
        self.widget_13.setObjectName("widget_13")
        self.tree_widget_accounts = QtWidgets.QTreeWidget(self.widget_13)
        self.tree_widget_accounts.setGeometry(QtCore.QRect(10, 250, 1110, 470))
        self.tree_widget_accounts.setFont(QtGui.QFont("Arial", 12))
        self.tree_widget_accounts.setStyleSheet("border: 1px solid rgb(100, 100, 100); border-radius: 5px;")
        self.tree_widget_accounts.setObjectName("tree_widget_accounts")
        self.label_account_number = QtWidgets.QLabel(self.widget_13)
        self.label_account_number.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label_account_number.setFont(QtGui.QFont("Arial", 12))
        self.label_account_number.setObjectName("label_account_number")
        self.lineEdit_account_number = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_account_number.setGeometry(QtCore.QRect(110, 20, 171, 31))
        self.lineEdit_account_number.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_account_number.setObjectName("lineEdit_account_number")
        self.label_branch_name = QtWidgets.QLabel(self.widget_13)
        self.label_branch_name.setGeometry(QtCore.QRect(310, 20, 91, 31))
        self.label_branch_name.setFont(QtGui.QFont("Arial", 12))
        self.label_branch_name.setObjectName("label_branch_name")
        self.lineEdit_branch_name = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_branch_name.setGeometry(QtCore.QRect(400, 20, 171, 31))
        self.lineEdit_branch_name.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_branch_name.setObjectName("lineEdit_branch_name")
        self.label_account_holder_id = QtWidgets.QLabel(self.widget_13)
        self.label_account_holder_id.setGeometry(QtCore.QRect(600, 20, 131, 31))
        self.label_account_holder_id.setFont(QtGui.QFont("Arial", 12))
        self.label_account_holder_id.setObjectName("label_account_holder_id")
        self.lineEdit_account_holder_id = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_account_holder_id.setGeometry(QtCore.QRect(730, 20, 171, 31))
        self.lineEdit_account_holder_id.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_account_holder_id.setObjectName("lineEdit_account_holder_id")
        self.label_balance = QtWidgets.QLabel(self.widget_13)
        self.label_balance.setGeometry(QtCore.QRect(20, 80, 61, 31))
        self.label_balance.setFont(QtGui.QFont("Arial", 12))
        self.label_balance.setObjectName("label_balance")
        self.lineEdit_balance = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_balance.setGeometry(QtCore.QRect(90, 80, 171, 31))
        self.lineEdit_balance.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_balance.setObjectName("lineEdit_balance")
        self.label_interest_rate = QtWidgets.QLabel(self.widget_13)
        self.label_interest_rate.setGeometry(QtCore.QRect(280, 80, 51, 31))
        self.label_interest_rate.setFont(QtGui.QFont("Arial", 12))
        self.label_interest_rate.setObjectName("label_interest_rate")
        self.lineEdit_interest_rate = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_interest_rate.setGeometry(QtCore.QRect(340, 80, 101, 31))
        self.lineEdit_interest_rate.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_interest_rate.setObjectName("lineEdit_interest_rate")
        self.label_time = QtWidgets.QLabel(self.widget_13)
        self.label_time.setGeometry(QtCore.QRect(460, 80, 71, 31))
        self.label_time.setFont(QtGui.QFont("Arial", 12))
        self.label_time.setObjectName("label_time")
        self.lineEdit_time = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_time.setGeometry(QtCore.QRect(540, 80, 101, 31))
        self.lineEdit_time.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.label_currency_type = QtWidgets.QLabel(self.widget_13)
        self.label_currency_type.setGeometry(QtCore.QRect(20, 140, 101, 31))
        self.label_currency_type.setFont(QtGui.QFont("Arial", 12))
        self.label_currency_type.setObjectName("label_currency_type")
        self.lineEdit_currency_type = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_currency_type.setGeometry(QtCore.QRect(130, 140, 171, 31))
        self.lineEdit_currency_type.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_currency_type.setObjectName("lineEdit_currency_type")
        self.label_input_amount = QtWidgets.QLabel(self.widget_13)
        self.label_input_amount.setGeometry(QtCore.QRect(330, 140, 101, 31))
        self.label_input_amount.setFont(QtGui.QFont("Arial", 12))
        self.label_input_amount.setObjectName("label_input_amount")
        self.lineEdit_input_amount = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_input_amount.setGeometry(QtCore.QRect(440, 140, 171, 31))
        self.lineEdit_input_amount.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_input_amount.setObjectName("lineEdit_input_amount")
        self.button_open_account = QtWidgets.QPushButton(self.widget_13)
        self.button_open_account.setGeometry(QtCore.QRect(80, 180, 121, 61))
        self.button_open_account.setFont(QtGui.QFont("Arial", 15))
        self.button_open_account.setStyleSheet("QPushButton {background-color:rgb(93, 255, 244); color: black; border-radius: 10px;}")
        self.button_open_account.setObjectName("button_open_account")
        self.button_close_account = QtWidgets.QPushButton(self.widget_13)
        self.button_close_account.setGeometry(QtCore.QRect(250, 180, 121, 61))
        self.button_close_account.setFont(QtGui.QFont("Arial", 15))
        self.button_close_account.setStyleSheet("QPushButton {background-color:red; color: white; border-radius: 10px;}")
        self.button_close_account.setObjectName("button_close_account")
        self.button_deposit = QtWidgets.QPushButton(self.widget_13)
        self.button_deposit.setGeometry(QtCore.QRect(420, 180, 121, 61))
        self.button_deposit.setFont(QtGui.QFont("Arial", 15))
        self.button_deposit.setStyleSheet("QPushButton {background-color:rgb(0, 0, 255); color: white; border-radius: 10px;}")
        self.button_deposit.setObjectName("button_deposit")
        self.button_withdraw = QtWidgets.QPushButton(self.widget_13)
        self.button_withdraw.setGeometry(QtCore.QRect(590, 180, 121, 61))
        self.button_withdraw.setFont(QtGui.QFont("Arial", 15))
        self.button_withdraw.setStyleSheet("QPushButton {background-color:rgb(0, 170, 255); color: white; border-radius: 10px;}")
        self.button_withdraw.setObjectName("button_withdraw")
        self.button_query_account = QtWidgets.QPushButton(self.widget_13)
        self.button_query_account.setGeometry(QtCore.QRect(760, 180, 121, 61))
        self.button_query_account.setFont(QtGui.QFont("Arial", 15))
        self.button_query_account.setStyleSheet("QPushButton {background-color:rgb(0, 170, 0); color: white; border-radius: 10px;}")
        self.button_query_account.setObjectName("button_query_account")
        self.button_clear_account = QtWidgets.QPushButton(self.widget_13)
        self.button_clear_account.setGeometry(QtCore.QRect(930, 180, 121, 61))
        self.button_clear_account.setFont(QtGui.QFont("Arial", 15))
        self.button_clear_account.setStyleSheet("QPushButton {background-color: rgb(170, 170, 170); color: white; border-radius: 10px;}")
        self.button_clear_account.setObjectName("button_clear_account")
        self.tabWidget.addTab(self.tab_account_management, "")

        # 贷款管理模块
        self.tab_loan_management = QtWidgets.QWidget()
        self.tab_loan_management.setObjectName("tab_loan_management")
        self.widget_17 = QtWidgets.QWidget(self.tab_loan_management)
        self.widget_17.setGeometry(QtCore.QRect(10, 0, 1130, 730))
        self.widget_17.setStyleSheet("background:rgb(250, 250, 250); border: 1px solid gray;")
        self.widget_17.setObjectName("widget_17")
        self.tree_widget_loans = QtWidgets.QTreeWidget(self.widget_17)
        self.tree_widget_loans.setGeometry(QtCore.QRect(10, 250, 1110, 470))
        self.tree_widget_loans.setFont(QtGui.QFont("Arial", 12))
        self.tree_widget_loans.setStyleSheet("border: 1px solid rgb(100, 100, 100); border-radius: 5px;")
        self.tree_widget_loans.setObjectName("tree_widget_loans")
        self.label_loan_id = QtWidgets.QLabel(self.widget_17)
        self.label_loan_id.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label_loan_id.setFont(QtGui.QFont("Arial", 12))
        self.label_loan_id.setObjectName("label_loan_id")
        self.lineEdit_loan_id = QtWidgets.QLineEdit(self.widget_17)
        self.lineEdit_loan_id.setGeometry(QtCore.QRect(110, 20, 171, 31))
        self.lineEdit_loan_id.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_loan_id.setObjectName("lineEdit_loan_id")
        self.label_branch = QtWidgets.QLabel(self.widget_17)
        self.label_branch.setGeometry(QtCore.QRect(310, 20, 91, 31))
        self.label_branch.setFont(QtGui.QFont("Arial", 12))
        self.label_branch.setObjectName("label_branch")
        self.lineEdit_branch = QtWidgets.QLineEdit(self.widget_17)
        self.lineEdit_branch.setGeometry(QtCore.QRect(400, 20, 171, 31))
        self.lineEdit_branch.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_branch.setObjectName("lineEdit_branch")
        self.label_loan_amount = QtWidgets.QLabel(self.widget_17)
        self.label_loan_amount.setGeometry(QtCore.QRect(600, 20, 91, 31))
        self.label_loan_amount.setFont(QtGui.QFont("Arial", 12))
        self.label_loan_amount.setObjectName("label_loan_amount")
        self.lineEdit_loan_amount = QtWidgets.QLineEdit(self.widget_17)
        self.lineEdit_loan_amount.setGeometry(QtCore.QRect(690, 20, 171, 31))
        self.lineEdit_loan_amount.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_loan_amount.setObjectName("lineEdit_loan_amount")
        self.label_repayment_plan = QtWidgets.QLabel(self.widget_17)
        self.label_repayment_plan.setGeometry(QtCore.QRect(20, 80, 91, 31))
        self.label_repayment_plan.setFont(QtGui.QFont("Arial", 12))
        self.label_repayment_plan.setObjectName("label_repayment_plan")
        self.lineEdit_repayment_plan = QtWidgets.QLineEdit(self.widget_17)
        self.lineEdit_repayment_plan.setGeometry(QtCore.QRect(110, 80, 171, 31))
        self.lineEdit_repayment_plan.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_repayment_plan.setObjectName("lineEdit_repayment_plan")
        self.label_borrower_id = QtWidgets.QLabel(self.widget_17)
        self.label_borrower_id.setGeometry(QtCore.QRect(310, 80, 91, 31))
        self.label_borrower_id.setFont(QtGui.QFont("Arial", 12))
        self.label_borrower_id.setObjectName("label_borrower_id")
        self.lineEdit_borrower_id = QtWidgets.QLineEdit(self.widget_17)
        self.lineEdit_borrower_id.setGeometry(QtCore.QRect(400, 80, 171, 31))
        self.lineEdit_borrower_id.setFont(QtGui.QFont("Arial", 12))
        self.lineEdit_borrower_id.setObjectName("lineEdit_borrower_id")
        self.button_clear_loan = QtWidgets.QPushButton(self.widget_17)
        self.button_clear_loan.setGeometry(QtCore.QRect(930, 140, 121, 61))
        self.button_clear_loan.setFont(QtGui.QFont("Arial", 15))
        self.button_clear_loan.setStyleSheet("QPushButton {background-color: rgb(170, 170, 170); color: white; border-radius: 10px;}")
        self.button_clear_loan.setObjectName("button_clear_loan")
        self.button_add_loan = QtWidgets.QPushButton(self.widget_17)
        self.button_add_loan.setGeometry(QtCore.QRect(80, 140, 121, 61))
        self.button_add_loan.setFont(QtGui.QFont("Arial", 15))
        self.button_add_loan.setStyleSheet("QPushButton {background-color:rgb(0, 170, 255); color: white; border-radius: 10px;}")
        self.button_add_loan.setObjectName("button_add_loan")
        self.button_delete_loan = QtWidgets.QPushButton(self.widget_17)
        self.button_delete_loan.setGeometry(QtCore.QRect(250, 140, 121, 61))
        self.button_delete_loan.setFont(QtGui.QFont("Arial", 15))
        self.button_delete_loan.setStyleSheet("QPushButton {background-color:red; color: white; border-radius: 10px;}")
        self.button_delete_loan.setObjectName("button_delete_loan")
        self.button_query_loan = QtWidgets.QPushButton(self.widget_17)
        self.button_query_loan.setGeometry(QtCore.QRect(420, 140, 121, 61))
        self.button_query_loan.setFont(QtGui.QFont("Arial", 15))
        self.button_query_loan.setStyleSheet("QPushButton {background-color:rgb(0, 170, 255); color: white; border-radius: 10px;}")
        self.button_query_loan.setObjectName("button_query_loan")
        self.button_issue_loan = QtWidgets.QPushButton(self.widget_17)
        self.button_issue_loan.setGeometry(QtCore.QRect(590, 140, 121, 61))
        self.button_issue_loan.setFont(QtGui.QFont("Arial", 15))
        self.button_issue_loan.setStyleSheet("QPushButton {background-color:rgb(255, 222, 90); color: black; border-radius: 10px;}")
        self.button_issue_loan.setObjectName("button_issue_loan")
        self.tabWidget.addTab(self.tab_loan_management, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "银行业务系统"))
        self.tree_widget_customers.headerItem().setText(0, _translate("MainWindow", "身份证号"))
        self.tree_widget_customers.headerItem().setText(1, _translate("MainWindow", "管理人身份证"))
        self.tree_widget_customers.headerItem().setText(2, _translate("MainWindow", "姓名"))
        self.tree_widget_customers.headerItem().setText(3, _translate("MainWindow", "联系电话"))
        self.tree_widget_customers.headerItem().setText(4, _translate("MainWindow", "家庭住址"))
        self.tree_widget_customers.headerItem().setText(5, _translate("MainWindow", "联系人姓名"))
        self.tree_widget_customers.headerItem().setText(6, _translate("MainWindow", "联系人手机号"))
        self.tree_widget_customers.headerItem().setText(7, _translate("MainWindow", "联系人Email"))
        self.tree_widget_customers.headerItem().setText(8, _translate("MainWindow", "联系人关系"))
        self.label_manager_id.setText(_translate("MainWindow", "管理人身份证"))
        self.label_customer_id.setText(_translate("MainWindow", "身份证号"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_phone.setText(_translate("MainWindow", "联系电话"))
        self.label_address.setText(_translate("MainWindow", "家庭住址"))
        self.label_contact_name.setText(_translate("MainWindow", "联系人姓名"))
        self.label_contact_phone.setText(_translate("MainWindow", "联系人电话"))
        self.label_contact_email.setText(_translate("MainWindow", "联系人Email"))
        self.label_contact_relation.setText(_translate("MainWindow", "联系人关系"))
        self.button_add_customer.setText(_translate("MainWindow", "添加"))
        self.button_delete_customer.setText(_translate("MainWindow", "删除"))
        self.button_update_customer.setText(_translate("MainWindow", "更新"))
        self.button_query_customer.setText(_translate("MainWindow", "查询"))
        self.button_clear_customer.setText(_translate("MainWindow", "清空"))
        self.button_avatar.setText(_translate("MainWindow", "上传头像"))
        self.label_avatar.setText(_translate("MainWindow", "头像预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_customer_management), _translate("MainWindow", "客户管理"))
        self.button_query_employees.setText(_translate("MainWindow", "查询员工"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_employee_management), _translate("MainWindow", "员工管理"))
        self.tree_widget_accounts.headerItem().setText(0, _translate("MainWindow", "账户号"))
        self.tree_widget_accounts.headerItem().setText(1, _translate("MainWindow", "支行名称"))
        self.tree_widget_accounts.headerItem().setText(2, _translate("MainWindow", "账户持有人ID"))
        self.tree_widget_accounts.headerItem().setText(3, _translate("MainWindow", "余额"))
        self.tree_widget_accounts.headerItem().setText(4, _translate("MainWindow", "利率"))
        self.tree_widget_accounts.headerItem().setText(5, _translate("MainWindow", "货币类型"))
        self.label_account_number.setText(_translate("MainWindow", "账户号"))
        self.label_branch_name.setText(_translate("MainWindow", "支行名称"))
        self.label_account_holder_id.setText(_translate("MainWindow", "账户持有人ID"))
        self.label_balance.setText(_translate("MainWindow", "余额"))
        self.label_interest_rate.setText(_translate("MainWindow", "利率"))
        self.label_time.setText(_translate("MainWindow", "开户时间"))
        self.label_currency_type.setText(_translate("MainWindow", "货币类型"))
        self.label_input_amount.setText(_translate("MainWindow", "输入金额"))
        self.button_open_account.setText(_translate("MainWindow", "开户"))
        self.button_close_account.setText(_translate("MainWindow", "销户"))
        self.button_deposit.setText(_translate("MainWindow", "存钱"))
        self.button_withdraw.setText(_translate("MainWindow", "取钱"))
        self.button_query_account.setText(_translate("MainWindow", "查询"))
        self.button_clear_account.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_account_management), _translate("MainWindow", "账户管理"))
        self.tree_widget_loans.headerItem().setText(0, _translate("MainWindow", "贷款号"))
        self.tree_widget_loans.headerItem().setText(1, _translate("MainWindow", "支行名称"))
        self.tree_widget_loans.headerItem().setText(2, _translate("MainWindow", "贷款金额"))
        self.tree_widget_loans.headerItem().setText(3, _translate("MainWindow", "还款计划"))
        self.tree_widget_loans.headerItem().setText(4, _translate("MainWindow", "借款人ID"))
        self.label_loan_id.setText(_translate("MainWindow", "贷款号"))
        self.label_branch.setText(_translate("MainWindow", "支行名称"))
        self.label_loan_amount.setText(_translate("MainWindow", "贷款金额"))
        self.label_repayment_plan.setText(_translate("MainWindow", "还款计划"))
        self.label_borrower_id.setText(_translate("MainWindow", "账户ID"))
        self.button_clear_loan.setText(_translate("MainWindow", "清空"))
        self.button_add_loan.setText(_translate("MainWindow", "申请贷款"))
        self.button_delete_loan.setText(_translate("MainWindow", "还款"))
        self.button_query_loan.setText(_translate("MainWindow", "查询贷款"))
        self.button_issue_loan.setText(_translate("MainWindow", "发放贷款"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_loan_management), _translate("MainWindow", "贷款管理"))
