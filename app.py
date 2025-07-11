from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bestallningar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Bestallning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(100), nullable=False)
    smaker = db.Column(db.String(200), nullable=False)
    adress = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('order.html')

@app.route('/order', methods=['POST'])
def order():
    namn = request.form['namn']
    adress = request.form['adress']
    smaker_lista = request.form.getlist('smaker')
    smaker_text = ', '.join(smaker_lista)

    ny = Bestallning(namn=namn, adress=adress, smaker=smaker_text)
    db.session.add(ny)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    if not os.path.exists('bestallningar.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
