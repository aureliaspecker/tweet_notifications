import os
from flask import Flask, render_template
import requests
from TwitterAPI import TwitterAPI

app = Flask("twitternotifications")

api = TwitterAPI(
    consumer_key = os.environ.get("consumer_key"),
    consumer_secret = os.environ.get("consumer_secret"),
    access_token_key = os.environ.get("access_token_key"),
    access_token_secret = os.environ.get("access_token_secret")
)

@app.route('/', methods=['GET'])
def display():
    endpoint = "https://api.twitter.com/1.1/account_activity/all/webhooks.json"
    #logic = thing_we_want()
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
