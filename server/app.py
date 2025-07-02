#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.before_request
def app_path():
    import os
    app.config['APP_PATH'] = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    user_agent = request.headers.get('User-Agent')
    method = request.method
    path = request.path
    query_string = request.query_string.decode()
    app_path = app.config.get('APP_PATH', 'Unknown')
    return f'''
        <h1>The host for this page is {host}</h1>
        <h2>The User-Agent is {user_agent}</h2>
        <h3>The request method is {method}</h3>
        <h4>The request path is {path}</h4>
        <h5>The query string is {query_string}</h5>
        <h6>The application path is {app_path}</h6>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    return f'<h1>Form Data: {data}</h1>'

@app.route('/headers')
def headers():
    headers = request.headers
    return f'<h1>Headers: {headers}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)