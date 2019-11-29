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
import psycopg2
from random import randint
app = Flask(__name__)


database_file = "postgresql://postgres:$shaurya1@localhost/testdb"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Longshorturl(db.Model):
    longurl = db.Column(db.String(200), unique=True, nullable=True, primary_key=True)
    shorturl = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<longurl:{},shorturl:{}>".format(self.longurl, self.shorturl)


db.create_all()
db.session.commit()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        try:
            shorturl = 'http://bitly_'+str(randint(1000, 9999))
            longurl = request.form.get("longurl")
            if longurl is None or longurl.strip()=='':
                return render_template("home.html", bool_empty=True)
            else:
                db.session.add(Longshorturl(longurl=longurl, shorturl=shorturl))
                db.session.commit()
                all_records = Longshorturl.query.order_by(Longshorturl.longurl).all()
                print(all_records)
                dict1={}
                for i in all_records:
                    print(i)
                    dict1[i.longurl] = i.shorturl
                return render_template('home.html', all_records=dict1)
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            a = request.form.get("longurl")
            try:
                var_shorturl = Longshorturl.query.filter_by(longurl=a).first().shorturl
                var_longurl = Longshorturl.query.filter_by(longurl=a).first().longurl
            except Exception as err:
                print('FunctionName: %s', err)
            return render_template("home.html", var_shorturl=var_shorturl, var_longurl=var_longurl)
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)