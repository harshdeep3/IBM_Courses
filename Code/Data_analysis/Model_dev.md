# Model Developement

This topic covers Linear Regression, Multiple Linear Regression and Polynomial Regression. Alongside these, it also cover the evaluation of the models.

## Linear Regression

Linear regression refers to one independent variable to make a prediction.

### Multiple Regression 
 Multiple Linear Regression refers to multiple independent variables to make a prediction. 

### Simple Linear Regression 
This is a method to understand the relationship between two variable:
* The predictor x
* The target y

This create the equation y = b0 + b1 * x, where b0 is the y intercept and b1 is the gradient (slope) .

Using Scikit-learn we can import models such as Linear Regression object. We then define the predictior and target variables. Then fit the model to the current data using **.fit(X, y)**. We can then use **.predict(X)** to predict the value for X.

## Multiple Linear Regression 

This is used to explain the relationship between:
* One continuous target (Y) variable
* Two or more predictor (X) variables 

This can be show using the equation y = b0 + b1 *x1 + b2 * x2 + ... + bn * xn. Where b0 is the y intercept and b1 to bn are the coefficients for the parameters x1 to xn.

This can be model using the same Linear Regression object. Multiple predictor variables are stored as the X input to the **fit()** method. Then the **predict()** method can be used. 


## Polynomial Regression




## Regression plot

By calling the function **seaborn.regplot()**, the regression can be plotted to a graph. 

## Residual Plot

The residual plot represents the error between the actual values. We obtain residual value by subtracting the predicting value and the actual target value. 

To plot the residual values, the function **residplot** from seaborn can be used. 

## Distribution Plot

A distribution plot counts the predicted value vs the actual value. The function **distplot** from seaborn can be used to display the distribution plot.

