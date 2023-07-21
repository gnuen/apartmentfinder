#!/usr/bin/env python3

from flask import Flask, request, jsonify
import encrypt
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'endpoint'])

@app.route("/")
def main():
    REQUEST_COUNT.labels('GET', '/').inc()
    return '''
     <form action="/echo_user_input" method="POST">
     Enter Name:<br/>
         <input name="user_input"><br/>Enter Password:
         <input name="pass_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/health")
def health():
    return jsonify(status='OK')

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    REQUEST_COUNT.labels('POST', '/echo_user_input').inc()
    user_input = request.form.get("user_input", "")
    pass_input = request.form.get("pass_input", "")
    return "You entered user: " + user_input + "<br/>You entered pass: " + encrypt.md5(pass_input)