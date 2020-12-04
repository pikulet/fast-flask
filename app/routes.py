from flask import render_template, redirect, url_for, request
from app import app, db
from app.forms import InputForm
from app.models import Text

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        return redirect(url_for('process', text=form.text.data))
    return render_template('input.html',
                           title='Input',
                           form=form)

@app.route('/process', methods=['GET'])
def process():
    value = request.args['text']

    existing_entry = Text.query.filter_by(text_value=value).first()
    if existing_entry is None:
        new_db_entry = Text(value)
        db.session.add(new_db_entry)
        db.session.commit()

    return render_template('index.html',
                           title='Input Received',
                           text=value)
