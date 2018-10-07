import os
from flask import Flask, render_template

from twitter import #thing_we_want

app = Flask("twitternotifications")


@app.route('/', methods=['GET'])
def display():
    logic = thing_we_want()
    return logic

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
