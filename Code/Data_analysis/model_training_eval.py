import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

def load_file(path):
    df = pd.read_csv(path)
    
    headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style", 
               "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type", 
               "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower", 
               "peak-rpm","city-mpg","highway-mpg","price"]
    # adding the columns headers
    df.columns = headers
    # replacing ? from nan
    df = df.replace('?', np.nan)
    
    return df



if __name__ == "__main__":
    

    # file path to load
    path = "Code/Data_analysis/data/file.csv"

    df = load_file(path=path)
    
    y_data = df['price']
    x_data = df.drop('price', axis=1)
    
    # training and test fit
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.20, random_state=1)
    
    # linear regression can be switched for any model
    lre = LinearRegression()
    
    # fit to data 
    lre.fit(x_train[['horsepower']], y_train)
    
    # r^2 score for test and train data 
    y_test_score = lre.score(x_test[['horsepower']], y_test)
    y_train_score = lre.score(x_train[['horsepower']], y_train)
    
    print(f"y_test score -> {y_test_score}, \n y_train score {y_train_score}")
    
    # cross validation score
    Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)
    
    print(f"r score -> {Rcross}")
    
    # prediction down by cross validation
    yhat = cross_val_predict(lre,x_data[['horsepower']], y_data,cv=4)
    yhat[0:5]
    
    
    