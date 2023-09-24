# Predict Iris Class


## Streamlit app to predict the species of Iris genus.

It can be used to predict which species does the folwer belong to under the genus *Iris*. It is Iris because the data that the model trained is the data about iris genus. The model predicts with help of the sepal and petal's width and length that we need to provide. Based on the data, it predicts the species as *setosa or versicolor or virginica*. 

This is a model from scikit-learn called *K Nearest Neighbors* aka KNN. KNN uses **euclidean distance** to learn and predict the data points. So it also called as *Lazy Algorithm*. But it is used in majority of supervised classification problems. 

Not only training the model and getting the best accuracy score is important. Also the deployment of the model is so important. The model has to be deployed to cloud or API in order to use it the fullest. So for deployment, I've used `streamlit`. 
