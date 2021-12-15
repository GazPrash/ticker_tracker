# for web frontend interfaces
from flask import Flask, jsonify, request
from flask_cors import CORS

from tickers import Ticker

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return """
                Ticker-Tracker API
                Developed By:- Prashant Shrivastava
                © 2021, All Rights Reserved
                Version:- 0.0.5
    
        """


@app.route("/search/download", methods=["GET"])  # ?Ticker_Name
def search():
    para = request.query_string.decode()
    tic1 = Ticker(para)
    if (tic1.find_dataframe()).empty:
        return jsonify("We have no information regarding that ticker")
    else:
        return jsonify(tic1.df)
    ...

@app.route("/analyze/solo")  # ?Ticker_Name&mthd=A_Number&arg=
def analyze():
    para, req_str = request.query_string.decode().split("&mthd=")
    anls_method, arg = req_str.split("&arg=")
    tic1 = Ticker(para)
    tic1.plot_analysis(kind = anls_method, argument = arg)
    # initialize ticker instance for generating analysis results
    ...


@app.route("/analysis/compare")
def compare():
    para, anls_method = request.query_string.decode().split("&mthd=")
    # initialize ticker instance for comparison
