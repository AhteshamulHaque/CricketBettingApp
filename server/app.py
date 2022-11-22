from logging.config import dictConfig
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
   return "Home page"


if __name__ == '__main__':
   # TODO: set process name

   host = "ec2-3-108-193-180.ap-south-1.compute.amazonaws.com"
   port = 8080

   app.run(host, port, debug=True)