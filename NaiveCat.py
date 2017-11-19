import numpy as np
from sklearn.externals import joblib
from date_extr import guess_date
pipeline = joblib.load("NaiveMedCat.pkl")

def prediction(example):
    """Returns class with max probability"""
    
    date = guess_date(example)
    pred = pipeline.predict_proba([example])
    labels = ['medical_statements', 'medical_tests', 'operation_protocol', 'research_method']
    res = (labels[np.argmax(pred)], np.max(pred), date)
    return res