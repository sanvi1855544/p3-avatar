from flask import Flask, render_template
from crud.app_crud import app_crud

from __init__ import app

app.register_blueprint(app_crud)

@app.route("/")
def index():
    return render_template("index.html") #"Avatar Website"

#about pages
@app.route("/Gennalyn/")
def Gennalyn():
    return render_template("Gennalyn.html")

@app.route("/Kashish/")
def Kashish():
    return render_template("Kashish.html")

@app.route("/Ellen/")
def Ellen():
    return render_template("Ellen.html")

@app.route("/Sanvi/")
def Sanvi():
    return render_template("Sanvi.html")

#PBL pages
@app.route("/FindYourNation/")
def FindYourNation():
    return render_template("FindYourNation.html")

@app.route("/Training/")
def Training():
    return render_template("Training.html")

@app.route("/Purpose/")
def Purpose():
    return render_template("Purpose.html")



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

