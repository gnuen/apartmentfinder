#!/usr/bin/env python3

from flask import Flask, request
import encrypt

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
     Enter Name:<br/>
         <input name="user_input"><br/>Enter Password:
         <input name="pass_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    user_input = request.form.get("user_input", "")
    pass_input = request.form.get("pass_input", "")
    return "You entered user: " + user_input + "<br/>You entered pass: " + encrypt.md5(pass_input)