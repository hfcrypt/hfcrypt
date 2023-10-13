import os
import requests
import json
from flask import Flask, jsonify, render_template, request, send_file


app = Flask(__name__)


@app.route("/")
def index():
    return "HFCrypt Demo. Host Closed Source Code on Hugging Face Spaces. Try to inspect the source code. It's encrypted! Click the Files tab ^^^. The code is stored in the `app.hfc` file and the encryption token is stored in Secrets. Learn more on the <a href=\"https://github.com/fakerybakery/HFCrypt\">GitHub Repository</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
