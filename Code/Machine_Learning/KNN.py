import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

if __name__ == "__main__":
    
    # load data
    df = pd.read_csv("Code\\Machine_Learning\\Data\\teleCust1000t.csv")
    
    # print(f"head -> {df.head()}, \n value count {df['custcat'].value_counts()}")
    
    X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
    X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
    
    y = df['custcat'].values
    
    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
    print ('Train set:', X_train.shape,  y_train.shape)
    print ('Test set:', X_test.shape,  y_test.shape)
    
    k = 4
    #Train Model and Predict  
    neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
    
    yhat = neigh.predict(X_test)
    
    print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
    print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
