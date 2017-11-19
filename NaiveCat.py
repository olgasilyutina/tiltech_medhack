import numpy as np
from sklearn.externals import joblib
from date_extr import guess_date
pipeline = joblib.load("NaiveMedCat.pkl")

def prediction(example):
    """Returns class with max probability"""
    
    date = guess_date(example)
    pred = pipeline.predict_proba([example])
    labels = ['medical_statements', 'medical_tests', 'operation_protocol', 'research_method']
    npm = np.max(pred)
    if npm <= 0.7:
        res = ("other", 0, date)
    else:
        res = (labels[np.argmax(pred)], npm, date)
        
    return res