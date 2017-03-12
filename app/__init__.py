from flask import Flask

app = Flask(__name__)
app.config.from_object('config.CONFIG')


from app.handlers import *
app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
app.add_url_rule('/pipeline', view_func=PipelineHandler.as_view('pipeline'), methods=['POST'])