import os
from flask import Flask, request, Response, g, render_template, jsonify
import marko
import google.generativeai as genai
from flask_cors import CORS


app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/postdata', methods=["POST"])
def fetchdata():
    if request.method == 'POST':
        
        print(request.json)    
    return {'Gotit': 'Sir'}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
