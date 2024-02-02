import joblib
import pandas as pd
import numpy as np

ddd=np.zeros((1,195))
def predict(data):
    lr_model = joblib.load('lr_model.sav')
    ddd[0,0:8]=np.transpose(data)
    return lr_model.predict(ddd)

