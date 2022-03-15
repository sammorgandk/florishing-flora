from flask import Flask, jsonify
import requests

app = Flask(__name__)


def flipCapString(string):
    # reverse string parameter
    flipped_string = string[::-1]
    # capitalize output using shoutcloud.io api
    url = 'https://shoutcloud-io.p.rapidapi.com/SHOUT'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'shoutcloud-io.p.rapidapi.com',
               'x-rapidapi-key': 'ca731e6766msh1504a306e1c75c4p152d6ajsnb9e350665ca4'}
    payload = '{"INPUT": "{' + flipped_string + '"}'
    r = requests.request("POST", url, data=payload, headers=headers)
    result = r.text
    return result


@app.route('/')
def hello():
    print('Welcome to my FlipCap Project')
    return 'Hello! I can flip a string at route: /flip/your string here'


@app.route('/flip/<string>')
def flipRoute(string):
    flipped = flipCapString(string)
    return jsonify(flipped)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
