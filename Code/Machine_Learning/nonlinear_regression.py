
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    
    # load data
    df = pd.read_csv("Code\\Machine_Learning\\Data\\FuelConsumptionCo2.csv")
    
    # get the right columns
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    cdf.head(9)

    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]
    test = cdf[~msk]
    
    # linear regression
    regr = linear_model.LinearRegression()
    
    # copying the lab code
    # train data
    train_x = np.asanyarray(train[['ENGINESIZE']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])
 
    X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2)
    
    poly = PolynomialFeatures(degree=2)
    train_x_poly = poly.fit_transform(X_train)
    
    regr.fit(X_train, y_train)
    
    print ('Coefficients: ', regr.coef_)
    print ('Intercept: ', regr.intercept_)
    
    predicted_test_y_ = regr.predict(X_test)
    
    print(f"Accuracy: {regr.score(X_test,y_test)}")
    print(f"Mean absolute error: {mean_squared_error(predicted_test_y_, y_test)}")
    print(f"Residual sum of squares (MSE): {np.mean((predicted_test_y_ - y_test) ** 2)}")
    print(f"R2-score: {r2_score(y_test , predicted_test_y_)}")
