from app import db, Bestallning, app

with app.app_context():
    alla = Bestallning.query.all()
    for b in alla:
        print(b.id, b.namn, b.smaker, b.adress, b.timestamp)
