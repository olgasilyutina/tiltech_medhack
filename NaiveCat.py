import numpy as np
from sklearn.externals import joblib
pipeline = joblib.load("NaiveMedCat.pkl")

def prediction(example):
    """Returns class with max probability"""
    
    pred = pipeline.predict_proba([example])
    labels = ['medical_statements', 'medical_tests', 'operation_protocol', 'research_method']
    max_pred = (labels[np.argmax(pred)], np.max(pred))
    return max_pred