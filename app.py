from flask import Flask , render_template ,url_for,  request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db =SQLAlchemy(app)

class Todo(db.Model):
     id =db.Column(db.Integer,primary_key=True)
     FirstName =db.Column(db.string(100),nullable=False)
     Lastname =db.Column(db.string(100),nullable=False)
     Gender=db.Column(db.string(1),nullable=False)
     Birthdate=db.Column(db.Integer(10),nullable=False)
     Age =db.Column(db.Integer(2),nullable=False)
     Blood Group =db.Column(db.string(3),nullable=False)
     Address= db.Column(db.string(100),nullable=False)
     Mobile no=db.Column(db.Integer(10),nullable=False)
     Email Id = db.Column(db.string(100),nullable=False)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method =='POST':
        pass

    else:
         return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)