from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location', validators=[DataRequired()])
    open = StringField('Cafe Opening Times Eg: 08:00AM', validators=[DataRequired()])
    close = StringField('Cafe Closing Time Eg: 17:30PM', validators=[DataRequired()])
    coffee = SelectField('Caffee Rating',choices=("❤", "❤❤", "❤❤❤", "❤❤❤❤", "❤❤❤❤❤") , validators=[DataRequired()])
    wifi = SelectField('Wifi Strenght', choices=("💻", "💻💻", "💻💻💻", "💻💻💻💻", "💻💻💻💻💻"), validators=[DataRequired()])
    power = SelectField('Cafe Power Rating', choices=("⚡", "⚡⚡", "⚡⚡⚡", "⚡⚡⚡⚡", "⚡⚡⚡⚡⚡"), validators=[DataRequired()])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data, form.wifi.data, form.power.data])
        form = CafeForm()
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
