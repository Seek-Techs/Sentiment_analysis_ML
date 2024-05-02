import streamlit as st
from joblib import load

# load model
# Load the Model
load_model = load('logistic_reg.pkl')


# create title
st.title('Sentiment Analysis Model')

review = st.text_area('Enter your review:')

submit = st.button('Predict')

if submit:
    prediction = load_model.predict([review])

    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')