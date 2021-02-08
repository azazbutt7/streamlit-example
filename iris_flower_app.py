import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

data = load_iris()

st.write("""
    # Simple Iris Flower Data Application
""")

st.sidebar.header("User Input features")


def user_input_fetures():
    sepal_length = st.sidebar.slider('sepal_length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('sepal_width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('petal_length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('petal_width', 0.1, 2.5, 1.2)

    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width:': petal_width
    }

    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_fetures()
st.subheader("User Input Parameters:")
st.write(df)

iris = load_iris()
X = iris.data
y = iris.target




clf = RandomForestClassifier()
clf.fit(X, y)

prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader('Class labels and their correspoding index number:')
st.write(iris.target_names)

st.write('Prediction')
st.write(iris.target_names[prediction])

st.write('Prediction Probability')
st.write(prediction_prob)


