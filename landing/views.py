from flask import render_template
from landing import app

@app.route("/")
def landing():
	return render_template('landing.html')
