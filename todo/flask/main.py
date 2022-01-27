#from crypt import methods
from datetime import datetime
#from pydoc import describe
#from turtle import title
#from urllib import request
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{{User}}:{{Password}}@{{ip}}:{{port}}/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class to_do(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    dtm = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.title} - {self.desc}"

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method ==  "POST":
       title = request.form['title']
       desc = request.form['desc']
       todo = to_do(title=title, desc=desc) 
       db.session.add(todo)
       db.session.commit()
    allTodo = to_do.query.all()
    return render_template('index.html', allTodo = allTodo)
   
@app.route("/delete/<int:id>")
def delete(id):
    todo = to_do.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    allTodo = to_do.query.all()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method ==  "POST":
       title = request.form['title']
       desc = request.form['desc']
       todo = to_do.query.filter_by(id=id).first()
       todo.title = title
       todo.desc = desc
       db.session.add(todo)
       db.session.commit()
       return redirect("/")
    todo = to_do.query.filter_by(id=id).first()
    return render_template('update.html', todo = todo)
   
   
if __name__ == "__main__":
    app.run(debug=True, port = 8000)