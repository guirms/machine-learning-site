from flask import Flask, make_response, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getPredict', methods=['GET'])
@cross_origin()
def make_predict():
    text_request = request.args.get('text_request')
    return make_response(jsonify(f"O texto é: {text_request}" ))

# app.run()