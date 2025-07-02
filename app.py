from flask import Flask, render_template
from chat import conersation_hander

app = Flask(__name__)

conversation = []

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)