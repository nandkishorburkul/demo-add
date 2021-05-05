# Import libraries
import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import functions
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('income.html')


#@app.route('/logistic',methods=['POST'])

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        data = request.form
        result = functions.valpredict(data)        
        if int(result)== 1:
            prediction ='Bad Loan'
        else:
            prediction ='Good Loan'            
        return render_template("result.html", prediction = prediction)



if __name__ == '__main__':
    app.run(debug = True)