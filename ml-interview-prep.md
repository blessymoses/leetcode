### What are the main assumptions of a linear regression?
- A linear regression models a relationship between the dependant variable y and independant variable x
- Two main assumptions:
  - The relationship between the dependant variable y and the explanatory variables X is linear.
  - The residual errors from the regression fit are normally distributed.
### What are the most common types of linear regression?
- What are the most common estimation techniques for linear regression?
  - Ordinary Least Squares
  - Generalized Least Squares
  - Penalized Least Squares
    - L1 (LASSO)
    - L2 (Ridge)
### Describe the formula for logistic regression and how the algorithm is used for binary classification
### How does a Decision Tree decide on its splits?
- What is the criteria for a split point?
  - A decision tree can use the Information Gain to decide on the splitting criteria.
  - The decision tree is built in a top-down fashion, but the question is how do you choose which attribute to split at each node?
  - The answer is, find the feature that best splits the target class into the purest possible children nodes.
  - This measure of purity is called the information.
  - It represents the expected amount of information that would be needed to specify whether a new instance should be classified 0 or 1, given the example that reached the node.
  - Entropy on the other hand is a measure of impurity.
  - Now, by comparing the entropy before and after the split, we obtain a measure of information gain, or how much information we gained by doing the split using that particular feature.
  - Information Gain = Entropy before - Entropy after
  