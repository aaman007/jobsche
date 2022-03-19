from flask import Blueprint, jsonify


blp = Blueprint(
    'home',
    __name__,
    url_prefix=''
)


@blp.route('/hello', methods=['GET'])
def home():
    return 'Hello World!'


@blp.route('', methods=['GET'])
def data():
    return jsonify([{'data': 'Hello World'}])
