# -*- coding: utf-8 -*-

import json
from flask import Flask, Response, request, abort, jsonify, make_response
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS
from .utils import json_response

app = Flask(__name__)
CORS(app, origins='*', allow_headers=[
        'Content-Type', 'Accept'])

english_bot = ChatBot('Chatterbot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train('chatterbot.corpus.english')

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    res = {
        'error': 'Not found'
    }
    return make_response(jsonify(res), 404)

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to Chatterbot Example.'

@app.route("/api/bot", methods=['GET'])
def get_bot_response():
    if request.method != 'GET':
        abort(404)
    req = request.args.get('message')
    if not req:
        abort(404)
    message = english_bot.get_response(req)
    res = {
        'data': {
            'user': str(req).encode('utf8'),
            'bot': str(message).encode('utf8')
        }
    }
    return jsonify(res)
    #return str(message)
