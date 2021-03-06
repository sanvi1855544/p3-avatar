from __init__ import app
from flask import Flask, render_template, request
from crud.app_crud import app_crud
from crud.app_crud_api import app_crud_api

from Sanvi.templates.Sanvi import sanvi_bp
from Ellen.templates.Ellen import ellen_bp
from Gennalyn.templates.Gennalyn import gennalyn_bp
from Kashish.templates.Kashish import kashish_bp

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)

@app.route("/")
def index():
    import requests
    URL = "https://last-airbender-api.herokuapp.com/api/v1/characters/random"
    r = requests.get(url=URL)
    data = r.json()
    return render_template("index.html", data=data) #"Avatar Website"

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

@app.route("/Dinasour/")
def Dinasour():
    return render_template("Dinasour.html")

@app.route("/Hangman/")
def Hangman():
    return render_template("Hangman.html")

@app.route("/Snake/")
def Snake():
    return render_template("Snake.html")

@app.route("/water/")
def water():
    return render_template("water.html")

@app.route("/earth/")
def earth():
    return render_template("earth.html")

@app.route("/fire/")
def fire():
    return render_template("fire.html")

@app.route("/air/")
def air():
    return render_template("air.html")

@app.route("/FindYourCharacter/")
def FindYourCharacter():
    return render_template("FindYourCharacter.html")

@app.route("/favorite/")
def FavoriteCharacter():
    return render_template("favorite.html")

@app.route("/avatartime/")
def avatartime():
    return render_template("avatartime.html")

@app.route("/ricknmorty/")
def ricknmorty():
    return render_template("ricknmorty.html")

@app.route("/ExploreCharacters/")
def ExploreCharacters():
    import requests
    URL = "https://last-airbender-api.herokuapp.com/api/v1/characters/random"
    r = requests.get(url=URL)
    data = r.json()
    return render_template("ExploreCharacters.html", data=data)





@app.route('/lookup')
def lookup():

    query = request.args.get('lookup')
    # req_search = query.filter_by(req_no=query)

    page = query+'.html'
    from pathlib import Path
    my_file = Path("templates/"+page)
    if my_file.exists():
        return render_template(page)
    else:
        return render_template('lookup.html', req_search=query)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

app.register_blueprint(sanvi_bp)
app.register_blueprint(ellen_bp)
app.register_blueprint(gennalyn_bp)
app.register_blueprint(kashish_bp)