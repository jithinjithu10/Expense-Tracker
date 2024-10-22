
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Expense

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        expense_name = request.form.get('name')  # Fetching the 'name' field from the form
        if not expense_name:
            return "Error: Expense name is required", 400  # If 'name' is missing, return error

        new_expense = Expense(name=expense_name)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to the index page after success
