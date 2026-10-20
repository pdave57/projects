PROJECT FILE SYSTEM.
personal_budget_tracker/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transaction.py
│   │   ├── category.py
│   │   └── budget.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── transaction.py
│   │   ├── category.py
│   │   └── budget.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── transactions.py
│   │   ├── categories.py
│   │   ├── budgets.py
│   │   └── reports.py
│   │
│   ├── services/
│   │   ├── transaction_service.py
│   │   ├── budget_service.py
│   │   └── report_service.py
│   │
│   └── repositories/
│       ├── transaction_repository.py
│       └── category_repository.py
│
├── tests/
│   ├── test_transactions.py
│   └── test_reports.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

Personal Budget Tracking System Using Python FastAPI
Let's design a Personal Budget Tracking System API that records income and expenses, organizes transactions by category, and calculates financial summaries for each category.

We'll use Python, FastAPI, SQLAlchemy, and PostgreSQL for the project. The application will follow a layered architecture so that you can extend it later with a React frontend, Flutter mobile application, and AI-powered spending recommendations.
1. Project Requirements
The system should support the following features.
A. Income management
- Record income from salary, business, freelance work, investments, and other sources.
- Assign each income transaction to a category.
- Calculate total income by category.
- Filter income by date range.

B. Expense management
- Record expenses such as food, rent, transportation, utilities, and entertainment.
- Assign expenses to categories.
- Calculate total expenses for each category.
- Identify the categories with the highest spending.

C. Financial calculations
The system should calculate:
1. Total income.
2. Total expenses.
3. Net cash flow.
4. Income by category.
5. Expenses by category.
6. Percentage of total expenses spent in each category.
7. Remaining budget for each category.
8. Monthly income and expense summaries.

D. Budget management
Users should be able to:
- Set spending limits for each expense category.
- Track actual spending against those limits.
- Calculate the remaining budget.
- Identify categories that exceed their budgets.

4. Database Design
The core database consists of three tables.
Table 1: Categories
A category classifies each transaction.
Column	Type	Description
id	Integer	Primary key
name	String	Category name
type	String	Income or expense


Example records:
id	name	type
1	Salary	income
2	Business	income
3	Food	expense
4	Transportation	expense
5	Rent	expense
6	Utilities	expense
7	Entertainment	expense


For a multi-user application, categories should also support ownership or shared default categories.
Table 2: Transactions
This table stores every income and expense record.
Column	Type	Description
id	Integer	Primary key
category_id	Integer	Category reference
type	String	Income or expense
amount	Numeric	Transaction amount
description	String	Transaction details
transaction_date	Date	Transaction date
created_at	DateTime	Record creation date


Important: Use NUMERIC(14,2) or Python's Decimal for monetary values rather than floating-point numbers.
Table 3: Budgets
Column	Type	Description
id	Integer	Primary key
category_id	Integer	Expense category
amount	Numeric	Budget limit
month	Integer	Budget month
year	Integer	Budget year


For example, a user can set a monthly food budget of ₦80,000 for October 2026.

The application will compare that limit with the total food expenses recorded during October.
5. Install the Dependencies
On Ubuntu, create the project and virtual environment:
mkdir personal_budget_tracker
cd personal_budget_tracker

python3 -m venv venv
source venv/bin/activate

Install the required packages:
pip install fastapi "uvicorn[standard]" sqlalchemy \
psycopg[binary] pydantic-settings alembic pytest httpx

Save the dependencies:
pip freeze > requirements.txt

For the initial implementation, we'll use SQLite to make testing easier. You can switch to PostgreSQL by changing the database configuration.