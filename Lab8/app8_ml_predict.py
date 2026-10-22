import joblib
import numpy as np
import streamlit as st

st.title("Iris Flower Prediction")

model = joblib.load("model.pkl")
classes = ["Setosa", "Versicolor", "Virginica"]

with st.form("prediction_form"):
    sl = st.slider("Sepal Length", 4.0, 8.0, 5.1)
    sw = st.slider("Sepal Width", 2.0, 4.5, 3.5)
    pl = st.slider("Petal Length", 1.0, 7.0, 1.4)
    pw = st.slider("Petal Width", 0.1, 2.5, 0.2)
    submit = st.form_submit_button("Predict")

if submit:
    features = np.array([[sl, sw, pl, pw]])
    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    
    st.success(f"Prediction: **{classes[pred]}**")
    st.metric("Confidence", f"{max(proba) * 100:.1f}%")

# Exercise 1: Bar chart of class probabilities

if submit :
    proba = model.predict_proba(features)[0]
    import pandas as pd
    proba_df = pd.DataFrame({"Class": classes, "Probability": proba})
    st.bar_chart(proba_df.set_index("Class"))

# Exercise 2: Prediction history

import pandas as pd
import streamlit as st

if "history" not in st.session_state:
  st.session_state.history = []

if submit:
  st.session_state.history.append({
      "SL": sl,
      "SW": sw,
      "PL": pl,
      "PW": pw,
      "Prediction": classes[pred],
  })

st.subheader("Prediction History")

if st.session_state.history:
  st.dataframe(pd.DataFrame(st.session_state.history))

# Exercise 3: Logistic Regression comparison

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200).fit(X, y)
joblib.dump(model, "model.pkl")
print("Logistic Regression model saved!")
