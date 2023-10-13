import os
from flask import render_template, request, Blueprint, send_from_directory
from app import db

from sqlalchemy import or_
from flask_sqlalchemy import SQLAlchemy
from flask import flash, redirect, url_for
from flask import render_template, send_from_directory
from flask import (Blueprint, Response, current_app, flash, jsonify, redirect,
                   render_template, request, send_from_directory, url_for)
from flask_sqlalchemy import SQLAlchemy
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Blueprints
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/start')
def index():
    return render_template('main/home.html')