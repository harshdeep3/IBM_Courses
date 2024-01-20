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
    data = data.replace('?', np.NaN)
    
    # get top 5 rows
    # print(data.head())
    
    # get statistical summary
    print(data.describe(include='all'))
