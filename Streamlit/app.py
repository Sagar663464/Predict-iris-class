import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


class Webpage:

    def __init__(self):
     
        self.title()
        self.data_split()
        self.model_fit()
        self.get_input()
        self.score()
        self.predict()
        self.plot()
    

    def title(self):
        st.markdown(f'<h1 style = "text-align : center">Predict Iris Class</h1>', unsafe_allow_html=True)
        img = Image.open('iris_in_vase_copy.jpg')
        st.image(img, caption='Iris flowers on vase')
        return


    def data_split(self):
        global data, df
        data = load_iris()
        df = pd.DataFrame(data['data'], columns=data['feature_names'])
        global x_train, x_test, y_train, y_test 
        x_train, x_test, y_train, y_test = train_test_split(data['data'], data['target'], train_size=0.8, random_state=2)
        return


    def model_fit(self):
        global model
        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(x_train, y_train)
        return
    

    def get_input(self):
        global sepal_l, sepal_w, petal_l, petal_w, pred_arr
        sepal_l = st.number_input('Sepal Length : ')
        sepal_w = st.number_input('Sepal Width : ')
        petal_l = st.number_input('Petal Length : ')
        petal_w = st.number_input('Petal Width : ')
        pred_arr = [sepal_l, sepal_w, petal_l, petal_w]

        global button
        button = st.button('Predict')
        return


    def predict(self):
        global  y_pred
        if button:
            y_pred = model.predict([pred_arr])
            pred = data['target_names'][y_pred]
            st.success(f"Predicted Class : {pred}")
        return
    

    def score(self):
        st.write('Model Accuracy:',model.score(x_test, y_test) * 100, '%')
        return
        

    def plot(self):
        st.write('Data: :chart_with_upwards_trend:')
        plot = px.scatter(df)
        st.plotly_chart(plot)
        return


if __name__ == '__main__':
    iris = Webpage()
    
