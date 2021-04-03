from flask import Flask, render_template, flash, redirect, request, session, url_for, Response
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/mysqldb'.format(user='root',
                                                                                                    password='root',
                                                                                                    host='localhost',
                                                                                                    database='mysqldb',
                                                                                                    auth_plugin='mysql_native_password')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Number2(db.Model):
    np = db.Column(db.String(250), primary_key=True)
    number = db.Column(db.String(250), unique=True)

@app.route('/store_number/', methods=['GET', 'POST'])
def store():
    if request.method == "POST":
        np = request.form['number_plate']
        number = request.form['phone_number']
        new_user = Number2(np=np,number=number)

        db.session.add(new_user)
        db.session.commit()
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.11.0', debug=True)