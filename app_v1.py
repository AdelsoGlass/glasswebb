from flask import Flask, render_template, request

app = Flask(__name__)

# Lista med glassorter
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
        beställning = request.form.getlist("glass")
        return render_template("order.html", namn=namn, beställning=beställning)
    return render_template("index.html", glassar=GLASSAR)

## if __name__ == "__main__":
##    app.run(host="0.0.0.0", port=5000, debug=True)

