
# Classification 
This is where you are categorizing some unknown items into a discrete set of categories or "classes".

Given a set of training data points, along with the target labels, classification determines the class label for an unlabeled test case. 

## K-nearest Neighbors (KNN)
This is based on the similarities to other cases. Data points that near each other are called "neighbors". Therefore, the distance between two cases is a measure of their dissimilarity. This can be done using Euclidean distance. 

## Decision Trees
Decision trees are built by splitting the training set into distinct nodes, where one node contains all of, or most of, one category of the data. 

## Logistic Regression
Logistic regression is similar to Linear regression. Where linear regression predicts continuous values of variables, logistic variables predicts categorical/discrete values instead of a numeric one. 

### Sigmoid function
This limits the output to be between 0 and 1. 

## Support Vector Machines (SVM)
SVM is a supervised algorithm that classifies cases by finding a separator. SVM first map data to high-dimensional feature space so that the data points can be categorised. Then a separator is is estimated for the data, the data should be transofmred in such a way that the separator could be drawn as a hyper-plane. 
For example if we have 2D data then the data is mapped to the 3D plane allowing for a separator to estimated. 


## Evaluation Metrics

### Jaccard Index (Jaccard Similarity coefficient)
Jaccard index can be defined as the size of the intersection divided by the size of the union of two labelled sets. For example:

y = [0,0,0,0,0,1,1,1,1,1]
y<sup>^</sup> = [1,1,0,0,0,1,1,1,1,1]
intersection of y and  y<sup>^</sup> is [0,0,0,1,1,1,1,1]. Meaning there are 8 value, so jaccard index is 8/(10+10-8) = 0.66. 

### F1-score
This uses a confusion matrix. The confusion matrix is used to calculate the precision and recall for the prediction model. Both these can be used to calculate the F1 score. 


### Log loss
This measures the performance of a classifier where the predicted output is a probability value between 0 and 1. Lower loss means better accuracy. 
