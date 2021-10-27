from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__)
app.secret_key = "Secret Key"

path = os.path.abspath( os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(path , 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Crud(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100))
    startDate = db.Column(db.String(100))
    endDate = db.Column(db.String(100))
    value = db.Column(db.String(100))
    risk = db.Column(db.String(100))

    def __init__(self, name, startDate, endDate, value, risk):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.value = value
        self.risk = risk

@app.route('/')
def index():
    all_data = Crud.query.all()
    return render_template("index.html", all_data = all_data)

# update function will be called into index.html to persist data.
@app.route('/insert', methods = ['POST'])
def insert():

    print('NOME: ' + request.form['name'])
    
    try:
        if request.method == 'POST':
            name = request.form['name']
            startDate = request.form['startDate']
            endDate = request.form['endDate']
            value = request.form['value']
            risk = request.form['risk']
            my_data = Crud(name, startDate, endDate, value, risk)
            db.session.add(my_data)
            db.session.commit()
        
        flash("Project Inserted Successfully")
        return redirect(url_for('index'))

    except:
        print("algo deu errado aqui!")


# update function will be called into index.html to edit and persist the data of the project.
@app.route('/update', methods = ['POST'])
def update():
    if request.method == "POST":
        my_date = Crud.query.get(request.form.get('id'))
        my_date.name = request.form['name']
        my_date.startDate = request.form['startDate']
        my_date.endDate = request.form['endDate']
        my_date.value = request.form['value']
        my_date.risk = request.form['risk']

        db.session.commit()
        flash("Project Updated Successfully")
        return redirect(url_for('index'))

# delete function will be called  into index.html to delete some row.
@app.route('/delete/<id>/')
def delete(id):
    my_data = Crud.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Project Data Deleted Successfully")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)

