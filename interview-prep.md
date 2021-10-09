## 12 Factor App
1. Codebase
    - Code is version controlled
    - One codebase tracked in revision control, many deploys
2. Dependencies
    - Explicitly declare and isolate the dependencies
3. Config
    - Store configurations in the environment
4. Backing Services
    - Treat backing resources as attached resources
5. Build, Release and Run
    - Strictly separate build and run stages
6. Processes
    - Execute the app as one or more stateless processes
7. Port Binding
    - Export services via port binding
8. Concurrency
    - Scale-out via the process model
9. Disposability
    - Maximize the robustness with fast startup and graceful shutdown
10. Dev/Prod parity
    - Keep development, staging and production as similar as possible
11. Logs
    - Treat logs as event streams
12. Admin processes
    - Run admin/management tasks as one-off processes

## Docker
### Containerization
- Containerization allows us to create an abstract representation of all the software applications.
- An image is created and any number of containers can be launched using the image, in any environment easily
### Docker
- Docker is a containerization tool or framework that allows us to package once and run anywhere.
- It implements the open container initiative standard and the docker image will have the entire infrastructure information along with the application itself.
### Docker components and workflow
- `Docker registry`: this is where all the docker images are stored centrally.
- `Docker Host` is the machine where docker engine is installed.
- `Docker client` gives the ability to run commands against the docker engine.
### Image Layers and Overlay
- A docker image is made up of multiple layers. It uses the concept of `Union File System` to integrate these layers together.
- When we pull an image, it pulls several layers, starting with the base kernel and then it will merge and all those layers are overlays one layer on top of another.
- When we pull the next time, it will pull only the layers that have changed.
### docker run
- Runs a command in a new container
- The docker run command first creates a writeable container layer over the specified image, and then starts it using the specified command.
- docker run is equivalent to the API /containers/create then /containers/(id)/start. 

## ML
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
### What advantages does a decision tree model have?
- Very easy to interpret and understand
- Works on both continuous and categorical features
- No normalization or scaling necessary
- prediction algorithm runs very fast
### What is the difference between a random forest versus boosting tree algorithms?
- Boosting Trees
  - Reassign weights to samples based on the results of previous iterations of classifications.
  - Harder to classify points get weighted more.
  - Iterative algorithm where each execution is based on the previous results.
- Random Forest
  - RF applies bootstrap aggregation to train many different trees.
  - This creates an ensemble of different individual decision trees.
  - In random forest algorithm, instead of using information gain or gini index for calculating the root node, the process of finding the root node and splitting the feature nodes will happen randomly.
### Given a dataset of features `x` and labels `y`, what assumptions are made when using Naive Bayes methods?
- Naive Bayes algorithm assumes that the features of `X` are conditionally independent of each other for the given `Y`.
- The idea that each feature is independent of each other may not always be true, but we assume it to be true to apply Naive Bayes. This "naive" assumption is where the namesake comes from.
### Describe how the support vector machine(SVM) algorithm works
