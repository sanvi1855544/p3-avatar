from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") #"Avatar Website"

@app.route("/Gennalyn/")
def Gennalyn():
    return render_template("Gennalyn.html") #"Avatar Website"

@app.route("/Kashish/")
def Kashish():
    return render_template("Kashish.html") #"Avatar Website"

@app.route("/Ellen/")
def Ellen():
    return render_template("Ellen.html") #"Avatar Website"

@app.route("/Sanvi/")
def Sanvi():
    return render_template("Sanvi.html") #"Avatar Website"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

