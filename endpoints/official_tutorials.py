from flask import Blueprint, redirect, url_for
from . import render_template

official_tutorials = Blueprint('official_tutorials', __name__)


@official_tutorials.route('/', methods=['GET'])
def official_tutorials_home():
    return render_template('pixijs_official_tutorials_home.html')
