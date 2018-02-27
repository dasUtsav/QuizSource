from flask import Flask, render_template
app = Flask(__name__)

@app.route('/all')
def display_all():
    return render_template("all.html")

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/description')
def description():
    return render_template("description.html")


if __name__ == "__main__":
    app.run(debug=True)
