import streamlit as st

# Streamlit web app title
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# Dropdown to select the operation
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Button to perform the calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"**Result**: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"**Result**: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"**Result**: {num1} * {num2} = {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"**Result**: {num1} / {num2} = {result}")
        else:
            st.error("Error! Division by zero.")

# Add a footer note
st.write("### Simple Calculator created with Streamlit!")
