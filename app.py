import shogun
from shogun import *
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(3)
    w = pickle.load(open("model.pkl","rb"))
    print (w)
    print (to_predict)
    result = w[0]*(to_predict[0])+w[1]*(to_predict[1])+(w[2]*(to_predict[2]))
    return result

@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        ans = ValuePredictor(to_predict_list)
        return render_template("index.html", ans=ans, x1=request.form['x1'], x2=request.form['x2'], x3=request.form['x3'])
    else:
        return flask.render_template('index.html', ans = -1, x1=0, x2=0, x3=0)


if __name__ == "__main__":
    app.run(debug=True)
