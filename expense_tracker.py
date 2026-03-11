import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit, QComboBox, QTableWidget, QDateEdit, \
    QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from PyQt5.QtCore import QDate,Qt

class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(670,600)
        self.setWindowTitle("Expense Tracker")
        self.dropdown = QComboBox()
        self.datebox = QDateEdit()
        self.datebox.setDate(QDate.currentDate())
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add")
        self.remove_button = QPushButton("Remove")
        self.add_button.clicked.connect(self.add_expense)
        self.remove_button.clicked.connect(self.remove_expense)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Id","Date","Category","Amount","Bills","Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.sortByColumn(1,Qt.DescendingOrder)

        self.dropdown.addItems(["Food","Transportation","Rent","Shopping","Entertainment"])

        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(QLabel("Date : "))
        self.row1.addWidget(self.datebox)
        self.row1.addWidget(QLabel("Category : "))
        self.row1.addWidget(self.dropdown)

        self.row2.addWidget(QLabel("Amount : "))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description : "))
        self.row2.addWidget(self.description)

        self.row3.addWidget(self.add_button)
        self.row3.addWidget(self.remove_button)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)
        self.load_table()

    def load_table(self):
        self.table.setRowCount(0)
        query = QSqlQuery("SELECT * FROM Expenses")
        row = 0
        while query.next():
            expennse_id = query.value(0)
            date = query.value(1)
            category = query.value(2)
            amount = query.value(3)
            description = query.value(4)

            self.table.insertRow(row)
            self.table.setItem(row,0,QTableWidgetItem(str(expennse_id)))
            self.table.setItem(row, 1, QTableWidgetItem(date))
            self.table.setItem(row, 2, QTableWidgetItem(category))
            self.table.setItem(row, 3, QTableWidgetItem(str(amount)))
            self.table.setItem(row, 4, QTableWidgetItem(description))
            row+=1

    def add_expense(self):
        date = self.datebox.date().toString("dd/MM/yyyy")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        query = QSqlQuery()

        query.prepare("""
                        INSERT INTO Expenses (date,category,amount,description)
                            VALUES (?,?,?,?)
                        """)
        query.addBindValue(date)
        query.addBindValue(category)
        query.addBindValue(amount)
        query.addBindValue(description)
        query.exec_()

        self.datebox.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

        self.load_table()
    def remove_expense(self):
        selected_row = self.table.currentRow()
        if selected_row==-1:
            QMessageBox.warning(self,"No expense is selected","Please choose an expense")
            return
        expense_id = int(self.table.item(selected_row,0).text())
        confirm = QMessageBox.question(self,"Are you sure?","Delete the item?",QMessageBox.Yes |QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        query = QSqlQuery()
        query.prepare("DELETE FROM Expenses WHERE id = ?")
        query.addBindValue(expense_id)
        query.exec_()
        self.load_table()



database = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("Expense.db")
if not database.open():
    QMessageBox.critical(None,"Error opening database")
    sys.exit(1)

query = QSqlQuery()
query.exec_("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
""")


if __name__ == "__main__":
    app = QApplication([])
    main = ExpenseTracker()
    main.show()
    app.exec_()



