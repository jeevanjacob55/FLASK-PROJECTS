from flask import Flask, render_template , request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,Email,URL
import csv 
app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
app.secret_key = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired(),URL()])
    open1 = StringField('Opening Time',validators = [DataRequired()])
    close = StringField('Closing Time',validators=[DataRequired()])
    coffee = SelectField(
        'Coffee Rating',
        choices=[
            ('☕', '☕'),
            ('☕☕', '☕☕'),
            ('☕☕☕', '☕☕☕'),
            ('☕☕☕☕', '☕☕☕☕'),
            ('☕☕☕☕☕', '☕☕☕☕☕')
        ],validators=[DataRequired()]
    )

    wifi = SelectField(
    'Wi-Fi Rating',
    choices=[
        ('✘', '✘'),
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪', '💪💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪')
    ])

    power = SelectField(
    'Power Rating',
    choices=[
        ('✘', '✘'),
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
    ])
    submit = SubmitField('Submit')





# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods =['GET','POST'])
def add_cafe():
    form = CafeForm()
    
    if form.validate_on_submit():
        name = request.form.get('cafe')
        location = request.form.get('location')
        open1 = request.form.get('open1')
        close = request.form.get('close')
        coffee = request.form.get('coffee')
        wifi = request.form.get('wifi')
        power = request.form.get('power')


        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name,location,open1,close,coffee,wifi,power])

    
        print("True")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
