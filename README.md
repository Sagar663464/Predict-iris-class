# Predict Iris Class


## Streamlit app to predict the species of Iris genus.

It can be used to predict which species does the folwer belong to under the genus *Iris*. It is Iris because the data that the model trained is the data about iris genus. The model predicts with help of the sepal and petal's width and length that we need to provide. Based on the data, it predicts the species as *setosa or versicolor or virginica*. 

This is a model from scikit-learn called *K Nearest Neighbors* aka KNN. KNN uses **euclidean distance** to learn and predict the data points. So it also called as *Lazy Algorithm*. But it is used in majority of supervised classification problems. 

Not only training the model and getting the best accuracy score is important. Also the deployment of the model is so important. The model has to be deployed to cloud or API in order to use it the fullest. So for deployment, I've used `streamlit`. 

## Requirements
- pandas
- numpy
- streamlit
- scikit-learn
- plotly
- Pillow


## Instructions to use
I've deployed the app, so you can visit https://predict-iris-class.streamlit.app/ to use the app from any device or browser as per your wish. If you like to run the source code yourself, 
- Download the files from the repo.   `git clone https://github.com/Sagar663464/Predict-iris-class`
  
- Open the folder in any IDE.
- Open up terminal.
- Change the directory to folder that has the files. `cd Predict-iris-class`

- Install required libraries.  `pip install requirements.txt`
  
- Run `streamlit run app.py`
- This will open up the app in a new tab in your default browser.

## Screenshots
![Screenshot 1](https://github.com/Sagar663464/Predict-iris-class/assets/65543059/247ac2b4-3391-4ff9-b094-ce888ee47de0)


![Screenshot 2](https://github.com/Sagar663464/Predict-iris-class/assets/65543059/256a9e36-683e-4270-82ef-886a60b102da)
