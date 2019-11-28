#folder structure of flask
'''
/myapplication.py
/schema.sql
/static
    /style.css
/templates
    /layout.html
    /index.html
HTTP response status codes indicate whether a specific HTTP request has
been successfully completed. Responses are grouped in five classes:

    Informational responses (100–199),
    Successful responses (200–299),
    Redirects (300–399),
    Client errors (400–499),
    and
    Server errors (500–599).
Refere this tutorial https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
'''
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from random import randint
app = Flask(__name__)


database_file = "postgresql://postgres:$shaurya1@localhost/testdb"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Longshorturl(db.Model):
    longurl = db.Column(db.String(200), unique=True, nullable=False, primary_key=True)
    shorturl = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<longurl:{},shorturl:{}>".format(self.longurl, self.shorturl)


db.create_all()
db.session.commit()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        try:
            shorturl = 'http://bitly/'+str(randint(1000, 9999))
            db.session.add(Longshorturl(longurl=request.form.get("longurl"), shorturl=shorturl))
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            a=request.form.get("longurl")
            var_shorturl = Longshorturl.query.filter_by(longurl=a).first()
            context = {}
            print(var_shorturl.longurl, var_shorturl.shorturl)
            context[request.form.get("longurl")] = var_shorturl
            print(context)
            len_dict = len(context)
            return render_template("home.html", var_context1=context, dictlen=len_dict)
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)