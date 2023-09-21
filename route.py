from flask import Flask, render_template, request, redirect, url_for, flash

from Models import db, User, Product, Category, Cart, Order

from app import app

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('Invalid user.')
        return redirect(url_for('login'))
    if not user.check_password(password):
        flash('Invalid password.')
        return redirect(url_for('login'))
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login_post():
    return "hello"    

@app.route('/register')
def register():
    return render_template('register.html')