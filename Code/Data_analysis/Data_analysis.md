
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


### Description Statistics

You are able to summaries the data using *describe()* method, it show the following data:
* Count
* Mean
* Standard deviation 
* Min
* 25%
* 50% 
* 75%
* Max

You can summaries the categorical data by using the *value_counts()* method.

### ANOVA

ANOVA stands for ANalysis of Variance. 

This finds the correlation between different groups of a categorical variable.

ANOVA returns the:
* F-test score: variation between sample group means divided by variation within sample group. 
* p-value: confidence score. 

### Pearson Correlation 
Measures the strength of the correlation between two features. It gives 2 values:
* Correlation coefficient 
* P-value 

This can be calculated using the Scipy stats package

Correlation coefficient 
* Close to +1 : Large **positive** relationships
* Close to -1 : Large **negative** relationships
* Close to 0 : **No** relationships

P-Value  
* P-Value < 0.001: **Strong** certainty in the result
* P-Value < 0.05: **Moderate** certainty in the result
* P-Value < 0.1: **Weak** certainty in the result
* P-Value > 0.1: **No** certainty in the result

