import json
from flask import Flask, Response, request, abort
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from .utils import json_response

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")

@app.route("/bot")
def get_bot_response():
    req = request.args.get('t')
    message =  english_bot.get_response(req)
    return str(message)

@app.errorhandler(404)
def not_found(e):
    return '', 404
