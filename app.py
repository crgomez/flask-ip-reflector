from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def report_ip():
      return request.remote_addr, 200

# Serving Flask App with Waitress via app-waitress.py
# app.run(host="0.0.0.0", port=80, debug=True)
