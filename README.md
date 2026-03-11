# 💰 Expense Tracker

A simple desktop **Expense Tracker** application built with **Python** and **PyQt5**. It allows users to add, view, and delete daily expenses stored in a local SQLite database.

---

## 🖥️ Features

- Add expenses with date, category, amount, and description
- Remove selected expenses with confirmation prompt
- View all expenses in a sortable table
- Data stored locally using SQLite database
- Clean and simple GUI built with PyQt5

---

## 📸 Screenshots

> Add a screenshot of your app here after running it.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| PyQt5 | GUI framework |
| SQLite | Local database storage |
| QSqlDatabase | Database connection via Qt |

---

## 📁 Project Structure

```
expense-tracker/
│
├── expense_tracker.py   # Main application file
├── Expense.db           # SQLite database (auto-created on first run)
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2. Install Dependencies
Make sure Python 3 is installed, then run:
```bash
pip install PyQt5
```

### 3. Run the Application
```bash
python expense_tracker.py
```

> The SQLite database `Expense.db` will be created automatically on first run.

---

## 🚀 How to Use

1. **Select a Date** using the date picker
2. **Choose a Category** from the dropdown (Food, Transportation, Rent, Shopping, Entertainment)
3. **Enter Amount** in the amount field
4. **Enter Description** (optional note about the expense)
5. Click **Add** to save the expense
6. Click on any row and press **Remove** to delete an expense

---

## 🐛 Known Issues / Bug Fixes

The following bugs are present in the current code and should be noted:

| Bug | Location | Description |
|---|---|---|
| Column count mismatch | `setColumnCount(5)` but 6 headers set | Change to `setColumnCount(6)` or remove "Bills" header |
| Table name case mismatch | CREATE TABLE uses `expenses` (lowercase), SELECT uses `Expenses` | Use consistent casing |
| `load_table` maps only 5 columns | Description mapped to column 4 instead of 5 | Update column index |

---

## 📌 Requirements

```
Python >= 3.7
PyQt5 >= 5.15
```

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Your Name**
- GitHub: [@MaxMad-coder](https://github.com/MaxMad-coder)
- Email: manash212005@gmail.com
