from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Konfigurera sökväg till SQLite-databasen
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bestallningar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Databastabell för beställningar
'''
class Bestallning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(50), nullable=False)
    glassorter = db.Column(db.String(200), nullable=False)
    tidpunkt = db.Column(db.DateTime, default=datetime.utcnow)
'''
class Bestallning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100))
    smaker = db.Column(db.String(200))     # ← viktigt!
    adress = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Glasslista
GLASSAR = [
    {"namn": "Vanilj", "pris": 25},
    {"namn": "Choklad", "pris": 30},
    {"namn": "Jordgubb", "pris": 28},
    {"namn": "Salt karamell", "pris": 35},
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        namn = request.form.get("namn")
        bestallning = request.form.getlist("glass")
        glass_text = ", ".join(bestallning)

        # Spara i databasen
        ny = Bestallning(namn=namn, smaker=glass_text)
        db.session.add(ny)
        db.session.commit()

        return render_template("order.html", namn=namn, beställning=bestallning)

    return render_template("index.html", glassar=GLASSAR)

# Visa alla beställningar (adminvy)
@app.route("/admin")
def admin():
    alla = Bestallning.query.order_by(Bestallning.tidpunkt.desc()).all()
    return render_template("admin.html", bestallningar=alla)

