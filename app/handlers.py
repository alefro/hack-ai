from flask import request, render_template
from flask_restful import Resource


class BaseHandler(Resource):
    def __init__(self):
        pass


class IndexHandler(BaseHandler):
    def dispatch_request(self):
        return render_template('index.html')

