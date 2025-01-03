from flask import Flask, render_template, request, flash,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from mailing import send_email

app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #The SQLALCHEMY_DATABASE_URI configuration tells Flask-SQLAlchemy where to locate the database.
db = SQLAlchemy(app) # initializes the SQLAlchemy extension in your Flask application and sets up the connection between your Flask app and the database.


class Form(db.Model):  #db.Model is a base class provided by SQLAlchemy that connects the model to your database.
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))



@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":  #In Flask, the request object is used to access the data and metadata of an incoming HTTP request made to the server.
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date,"%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date=date_obj,
            occupation=occupation
        )
        db.session.add(form)
        db.session.commit()
        send_email(first_name,last_name,email,date,occupation)
        flash(f"{first_name},Your form is submitted successfully","success")
        return redirect(url_for("index"))
        #The url_for() function generates the URL for a given view function dynamically based on the function's name.
        # Instead of hardcoding the URL (like "/"), url_for() ensures that the correct URL is generated even if the route changes later. It uses the function name as its argument and looks up the route associated with that function.


    return render_template("index.html")

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True,port=5001)

