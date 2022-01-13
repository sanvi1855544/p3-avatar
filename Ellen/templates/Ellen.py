from flask import Blueprint, render_template, request

ellen_bp = Blueprint('Ellen', __name__,
                        url_prefix='/Ellen',
                        template_folder='templates',
                        static_folder='static', static_url_path='static/Ellen')

@ellen_bp.route("/", methods=['GET','POST'])
def ellen_index():

    return render_template("Ellen.html")