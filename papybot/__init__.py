from flask import Flask
"""Flask modul init"""
app = Flask(__name__)

from . import views_web
