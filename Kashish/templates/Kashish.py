from flask import Blueprint, render_template, request

kashish_bp = Blueprint('Kashish', __name__,
                     url_prefix='/Kashish',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/Kashish')

@kashish_bp.route("/", methods=['GET','POST'])
def kashish_index():

    return render_template("Kashish.html")