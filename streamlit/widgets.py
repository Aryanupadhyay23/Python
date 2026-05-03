import streamlit as st

st.title("Widgets in Streamlit")

st.header("Input Widgets")

# Text Input
st.subheader("Text Input")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Number Input
st.subheader("Number Input")
age = st.number_input("Enter your age:", min_value=0, max_value=120)
if age:
    st.write(f"You are {age} years old.")

# Select Box
st.subheader("Select Box")
color = st.selectbox("Select your favorite color:", ["Red", "Green", "Blue"])
st.write(f"Your favorite color is {color}.")

# Checkbox
st.subheader("Checkbox")
subscribe = st.checkbox("Subscribe to newsletter")
if subscribe:
    st.write("Thank you for subscribing!")

# Radio Buttons (FIXED)
st.subheader("Radio Buttons")
gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
st.write(f"Your gender is {gender}.")

# Multiselect
st.subheader("Multiselect")
hobbies = st.multiselect(
    "Select your hobbies:",
    ["Reading", "Traveling", "Cooking", "Sports"]
)
if hobbies:
    st.write(f"Your hobbies are: {', '.join(hobbies)}.")

# Date Input
st.subheader("Date Input")
date = st.date_input("Select a date:")
st.write(f"You selected: {date}")

# Time Input
st.subheader("Time Input")
time = st.time_input("Select a time:")
st.write(f"You selected: {time}")

# File Uploader
st.subheader("File Uploader")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(f"File name: {uploaded_file.name}")
    st.write(f"File type: {uploaded_file.type}")
    st.write(f"File size: {uploaded_file.size} bytes")