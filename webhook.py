# flask_ngrok_example.py
from flask import Flask, request
from flask_ngrok import run_with_ngrok
import json, time


app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/", methods=['POST', 'GET'])
def hello():
    print("new webhook received!")
    data = json.loads(request.data)
    print(data)

if __name__ == '__main__':
    app.run()  # If address is in use, may need to terminate other sessions:
               # Runtime > Manage Sessions > Terminate Other Sessions
