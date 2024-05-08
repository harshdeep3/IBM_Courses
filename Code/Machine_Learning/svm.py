import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn import svm


if __name__ == "__main__":
    df = pd.read_csv("Code\\Machine_Learning\\Data\\FuelConsumptionCo2.csv")
    
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    
    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]
    test = cdf[~msk]
    
    clf = svm.SVC()
    x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
    y = np.asanyarray(train[['CO2EMISSIONS']])
    clf.fit(x, y)
    
    #uncomplete the lab wasn't not working