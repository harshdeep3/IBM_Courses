# Model Evaluation

Model Evaluation tells us how the model performs in the real world. In-sample evaluation tells us how well our model fits the data already given to train it. 

The data is split into training, validation and test data. This allows us to evaluate the perform in the real world.

## Generalisation error

This error is the measure of how well our model does at predicting previously unseen data. The error we obtain using our testing data is an approximation of this error.

## Cross Validation 
Equal folds are create for the data. Each fold is used for both training and testing data.

For example if there 4 fold (1,2,3,4), then 1-3 will act as training data and 4 is test data for round 1. Then another combination of fold is used to train and test. So it could 1,2 and 4 are training data and 3 is test data. 

# Model Selection
When selecting a model, you can plot a graph with the MSE against the order of polynomial. When the lost MSE is produced that is the best model. Anything on the left is under-fitting and anything on the right is over-fitting. 

## Over fitting
When the model is too flexible and fits the noise rather than the function. 

## Under fitting 
When the model is not complex enough to fit the data, this is called under-fitting. 

# Ridge Regression
Ridge regression is used to prevent over-fitting. A variable alpha is used to add weight to the oder of polynomials. If alpha is too large, then under-fitting occurs and if the value is too small then over-fitting occurs. 

# Grid search 
Grid search allows us to scan through multiple free parameters with a few lines of code (hyper-parameter tuning). Grid search takes the model or objects you would like to train and different values of the hyper-parameter allowing you to choose the best values.  