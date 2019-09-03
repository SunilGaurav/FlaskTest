# app.py
from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance

data = {"URL": "Merchant","URL1": "Merchant1","URL2": "Merchant2","URL3": "Merchant3"}


@app.route("/businessClass/<website_url>", methods=["GET"])
def isSubscribed(website_url):
    return data[website_url]


if __name__ == "__main__":  # on running python app.py
    app.run(host="10.110.132.75",port ="8181")  # run the flask app
