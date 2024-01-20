import numpy as np
import pandas as pd
import matplotlib as plt

if __name__ == "__main__":
    

    # file path to load
    path = "Code/Data_analysis/data/file.csv"
    data = pd.read_csv(path)
    
    headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style", 
               "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type", 
               "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower", 
               "peak-rpm","city-mpg","highway-mpg","price"]
    
    # adding the columns headers
    data.columns = headers
    
    # replacing ? from nan
    data = data.replace('?', np.nan)
    
    # get top 5 rows
    print(data.head())
    
    # drop missing values 
    # inplace = True -> writes the results back into the dataframe
    # axis = 0 drops the entire row ---- axis =1 drops the entire column
    data.dropna(subset=["price"], axis=0, inplace=True)
    
    # replaces the str Nan with a float/int and converts the number as str to int 
    data["normalized-losses"] = data['normalized-losses'].replace('NaN', pd.NA).fillna(0).astype(int)
    
    # replacing the data with the average 
    mean = data['normalized-losses'].mean()
    data["normalized-losses"].replace(np.nan, mean)
    