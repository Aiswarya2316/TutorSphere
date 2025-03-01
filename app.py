from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('admin_side/index.html')

@app.route('/add_teacher')
def add_teacher():
    return render_template('admin_side/add_teacher.html')

@app.route('/add_book')
def add_book():
    return render_template('admin_side/add_book.html')

@app.route('/edit_book')
def edit_book():
    return render_template('admin_side/edit_book.html')

@app.route('/edit_teacher')
def edit_teacher():
    return render_template('admin_side/edit_teacher.html')

@app.route('/view_book')
def view_book():
    return render_template('admin_side/view_book.html')

@app.route('/view_teacher')
def view_teacher():
    return render_template('admin_side/view_teacher.html')
app.run()