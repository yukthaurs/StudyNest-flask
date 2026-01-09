
from flask import Flask, render_template

# This must be exactly 'app'
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
