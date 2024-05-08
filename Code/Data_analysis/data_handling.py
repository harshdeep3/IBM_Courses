import numpy as np
import pandas as pd
import matplotlib as plt

if __name__ == "__main__":
    

    # file path to load
    path = "Code/Data_analysis/data/file.csv"
    df = pd.read_csv(path)
    
    headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style", 
               "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type", 
               "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower", 
               "peak-rpm","city-mpg","highway-mpg","price"]
    
    # adding the columns headers
    df.columns = headers
    
    # replacing ? from nan
    df = df.replace('?', np.nan)
    
    # drop missing values 
    # inplace = True -> writes the results back into the dataframe
    # axis = 0 drops the entire row ---- axis =1 drops the entire column
    df.dropna(subset=["price"], axis=0, inplace=True)
    
    # replaces the str Nan with a float/int and converts the number as str to int 
    df["normalized-losses"] = df['normalized-losses'].replace('NaN', pd.NA).fillna(0).astype(int)
    
    # replacing the data with the average 
    mean = df['normalized-losses'].mean()
    df["normalized-losses"].replace(np.nan, mean)
    
    ####################################################
    ################# Normalisation ####################
    
    # Min-Max  
    df['length'] = (df['length'] - df['length'].min())/ (df['length'].max() - df['length'].min())
    
    # Z-score    
    df['width'] = (df['width'] - df['width'].mean())/ df['width'].std()
    
    ####################################################
    ##################### Binning ######################

    # convert str to int
    df['price'] = df['price'].astype(int)
    
    # create 4 bins
    bins = np.linspace(min(df['price']), max(df['price']), 4)
    group_names = ['Low', 'Medium', 'High']
    
    # cut data to bins
    df['price-binned'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)
    
    ####################################################
    ################# One_hot encoding #################
    
    one_hot_encodding = pd.get_dummies(df['fuel-type'])
    
    df = df.assign(Diesel=one_hot_encodding['diesel'].astype(int),
                   Gas=one_hot_encodding['gas'].astype(int))
    
    # get top 5 rows
    print(df.head())