from flask import Flask,jsonify, request
from dotenv import load_dotenv
import os
from wos_client import fetch_wos_data

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return  jsonify({'message': 'WOS backend is running'}),200

@app.route('/api/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error':'Query parameter is required'}),400
    
    try:
        results = fetch_wos_data(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error':str(e)}),500
    
if __name__ == '__main__':
    app.run(debug=True)