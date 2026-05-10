import streamlit as st
import pandas as pd
import joblib

model = joblib.load('titanic_model.pkl')

st.title("Titanic Survival Calculator")
st.write("Enter your details and check if you would survive!")

gender = st.selectbox("Select gender", ["Male", "Female"])
age = st.slider("How old are you?", 0, 100, 25)
ticket_class = st.selectbox("Ticket class", [1, 2, 3])
fare = st.number_input("Ticket fare (in dollars)", value=50)
family = st.slider("How many people are traveling with you?", 0, 10, 0)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

gender_machine = 0 if gender == "Male" else 1

is_q = False
is_s = False

if embarked == "Q":
    is_q = True
elif embarked == "S":
    is_s = True

if st.button("Calculate my chances!"):
    data = pd.DataFrame([[ticket_class, gender_machine, age, fare, family, is_q, is_s]],
                        columns=['Pclass', 'Sex', 'Age', 'Fare', 'FamilyMembers', 'Embarked_Q', 'Embarked_S'])

    chances = model.predict_proba(data)[0][1] * 100

    if chances > 50:
        st.success(f"Success! You have a {chances:.1f}% chance of survival. The lifeboat is waiting!")
        st.balloons()
    else:
        st.error(f"Unfortunately... Only a {chances:.1f}% chance. The band plays for you until the end.")