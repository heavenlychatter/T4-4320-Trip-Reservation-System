from flask import current_app as app
from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash


main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        if request.form.get("report_option") == "product_reports":
            return redirect(url_for('admin'))
        if request.form.get("report_option") == "customer_reports":
            return redirect(url_for('reservations'))
        else:
            flash("Invalid report option, try again.")
            return render_template('index.html')
        
@main_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    pass

@main_bp.route('/reservations', methods=['GET', 'POST'])
def reservations():
    pass


