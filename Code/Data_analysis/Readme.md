
# Data Analysis 

## Pre-processing 

### Handling missing data

* Drop missing values
    * drop the variable 
    * drop the data entry

* Replace the missing values 
    * replace it with an average (of similar data points)
    * replace it by frequency
    * replace it based on other functions

* Leave it as missing data

### Normalising 

* Simple Feature scaling 
    * dividing each value by the maximum value for the feature 
    * n_new = x_old/x_max
    * ranges between 0 and 1

* Min-Max
    * takes each value x_old substracted from the minimum value for a feature and divides by the range of the feature
    * n_new = (x_old - x_min)/(x_max - x_min)
    * ranges between 0 and 1

* z-score (standard score)
    *   subtract the Mu from each value divided by the standard deviation
        * Mu is the average of the feature
    *   x_new = (x_old - x_mu)/ standard_deviation
    * ranges between -3 and 3 