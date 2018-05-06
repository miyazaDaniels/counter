# coding: utf8
from flask import Flask, abort, make_response, request
import json
import os

app = Flask(__name__)

FILE_PATH = './count_file.txt'
GOOD_COUNT = 'good_count'

def to_response(obj, code=200):
    return app.response_class(
        response=json.dumps(obj, ensure_ascii=False),
        status=code,
        mimetype='application/json')

def create_dict(key, value):
    dict = {}
    dict['%s' % key] = value
    return dict

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
    return 'Welcome'

@app.route('/good', methods=['GET'])
def good():
    count = add_count()
    return to_response(create_dict(GOOD_COUNT, count))

@app.route('/reset', methods=['GET'])
def reset():
    count = reset_count()
    return to_response(create_dict(GOOD_COUNT, count))

@app.route('/get', methods=['GET'])
def get():
    count = get_count()
    return to_response(create_dict(GOOD_COUNT, count))

@app.route('/set', methods=['GET'])
def zet():
    count = request.args.get('count', type=int)
    if count is None:
        count = get_count()
    count = write_count(count)
    return to_response(create_dict(GOOD_COUNT, count))

if __name__ == '__main__':
    app.run()
