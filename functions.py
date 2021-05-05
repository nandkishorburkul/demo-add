import numpy as np
import pickle

def valpredict(data):
    loan_amnt = int(data['loan_amnt'])
    int_rate = float(data['int_rate'])
    emp_length = float(data['emp_length'])
    home_ownership = int(data['home_ownership'])
    annual_inc = float(data['annual_inc'])
    dti = float(data['dti'])
    delinq_2yrs = float(data['delinq_2yrs'])
    revol_util = float(data['revol_util'])
    total_acc = float(data['total_acc'])
    longest_credit_length = float(data['longest_credit_length'])
    
    if data['verification_status']=='verified':
    	verification_status = 0
    else:
    	verification_status = 1
    
    if data['term']=='36 months':
    	term = 0
    else:
    	term = 1
    loaded_model = pickle.load(open("model.pkl", "rb"))
    x_predict=[[loan_amnt,int_rate,emp_length,home_ownership,annual_inc,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status,term]]
    result = loaded_model.predict(x_predict)
    return result

    


