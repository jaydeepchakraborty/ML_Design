'''
python3 RestApiExample.py &
Running on http://127.0.0.1:5000
'''

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api

app = Flask(__name__)
CORS(app)

@app.route('/test_rest_post/', methods=['POST'])
def test_rest_api_post():
    try:
        req_ip = request.get_json()
        return req_ip
    except Exception as e:
        raise e
        
@app.route('/test_rest_get/', methods=['GET'])
def test_rest_api_get():
    try:
        return {"msg": "this is get method"}
    except Exception as e:
        raise e
        
        
if __name__ == "__main__":
    try:
        test_host = "127.0.0.1"
        test_port = 5000
        app.run(host=test_host, port=test_port)
    except Exception as e:
        raise e