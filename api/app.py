from flask import Flask, make_response, jsonify, request
from flask_cors import CORS, cross_origin
from ml import get_predict

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getPredict', methods=['GET'])
@cross_origin()
def make_predict():
    return make_response(jsonify(get_predict()))

@app.route('/teste', methods=['GET'])
@cross_origin()
def teste():
    return "so tapa"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)