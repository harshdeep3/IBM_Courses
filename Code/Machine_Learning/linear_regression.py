
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    
    # load data
    df = pd.read_csv("Code\\Machine_Learning\\Data\\FuelConsumptionCo2.csv")
    
    # get the right columns
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]
    test = cdf[~msk]
    
    # linear regression
    regr = linear_model.LinearRegression()
    
    # copying the lab code
    # train data
    train_x = np.asanyarray(train[['ENGINESIZE']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])
    
    regr.fit(train_x, train_y)
    
    # The coefficients
    print ('Coefficients: ', regr.coef_)
    print ('Intercept: ',regr.intercept_)
    
    # evaluaton
    test_x = np.asanyarray(test[['ENGINESIZE']])
    test_y = np.asanyarray(test[['CO2EMISSIONS']])
    test_y_ = regr.predict(test_x)

    print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
    print("R2-score: %.2f" % r2_score(test_y , test_y_) )
    
    print("......................................")
    print(f"\n\nTest code")
    # test code 
    X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2)
    
    regr.fit(X_train, y_train)
    
    predicted_test_y_ = regr.predict(X_test)
    
    print(f"Accuracy: {regr.score(X_test,y_test)}")
    print(f"Mean absolute error: {mean_squared_error(predicted_test_y_, y_test)}")
    print(f"Residual sum of squares (MSE): {np.mean((predicted_test_y_ - y_test) ** 2)}")
    print(f"R2-score: {r2_score(y_test , predicted_test_y_)}")
    
    ########################## Multiple Linear Regression ###########################
    
    print("\n\nMultiple Linear Regression\n")
    
    cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
    # print(f"\n\n\n{cdf.head(9)}")
    
    train_x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])
    
    X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.2)
    
    regr.fit(X_train, y_train)
    
    print(f"Coefficients {regr.coef_}")
    predicted_test_y_ = regr.predict(X_test)
    
    print(f"Accuracy: {regr.score(X_test,y_test)}")
    print(f"Mean absolute error: {mean_squared_error(predicted_test_y_, y_test)}")
    print(f"Residual sum of squares (MSE): {np.mean((predicted_test_y_ - y_test) ** 2)}")
    print(f"R2-score: {r2_score(y_test , predicted_test_y_)}")