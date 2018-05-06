# coding: utf8
from flask import Flask, abort, make_response, request
import json
import os

app = Flask(__name__)

global FILE_PATH
FILE_PATH = './count_file.txt'

def to_response(obj, code=200):
    return app.response_class(
        response=json.dumps(obj, ensure_ascii=False),
        status=code,
        mimetype='application/json')

def get_count():
    with open(FILE_PATH, 'r') as f:
        for line in f:
            count = int(line)

    return count

def add_count():
    count = get_count()
    count += 1
    count = write_count(count)

    return count

def write_count(count):
    with open(FILE_PATH, 'w') as f:
        f.write(str(count))

    return count

def reset_count():
    count = 0
    with open(FILE_PATH, 'w') as f:
        f.write(str(count))

    return count

@app.route('/')
def hello_world():
    return 'Welcome to Our Wedding Reception!'

@app.route('/good', methods=['GET'])
def good():
    count = add_count()
    response_dict = {}
    response_dict['good_count'] = count

    return to_response(response_dict)

@app.route('/reset', methods=['GET'])
def reset():
    count = reset_count()
    response_dict = {}
    response_dict['good_count'] = count
    return to_response(response_dict)

@app.route('/get', methods=['GET'])
def get():
    count = get_count()
    response_dict = {}
    response_dict['good_count'] = count
    return to_response(response_dict)

@app.route('/set', methods=['GET'])
def zet():
    count = request.args.get('count', type=int)
    if count is None:
        count = get_count()

    count = write_count(count)

    response_dict = {}
    response_dict['good_count'] = count

    return to_response(response_dict)

if __name__ == '__main__':
    app.run()
