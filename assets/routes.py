from flask import current_app as app
from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
from .forms import *


main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        if request.form.get("menu_option") == "admin":
            return redirect(url_for('main.admin'))
        if request.form.get("menu_option") == "reservations":
            return redirect(url_for('main.reservations'))
        else:
            flash("Invalid menu option, try again.")
            return render_template('index.html')
        
@main_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        form = LoginForm()
        if request.method == "GET":
            return render_template('admin.html', form=form)
    
    except Exception as e:
        flash("ERROR: unexpected login failure")
        print(f"{e}")
        return redirect(url_for('main.index'))



@main_bp.route('/reservations', methods=['GET', 'POST'])
def reservations():
    pass


