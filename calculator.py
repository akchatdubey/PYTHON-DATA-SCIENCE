import streamlit as st 


# a simple calculator
def calculator(a,b,op="+"):
    match (op):
        case '+':  return a + b
        case'minus': return a - b
        case '*': return a * b
        case'/': return a/b
        case'**':return a**b
        
st.title("Simple Calculator")
st.markdown("very simple and cheap")

c1 ,c2,c3 = st.columns(3)
num1 = c1.number_input("Enter first number",value=62)
num2 = c2.number_input( "Enter second number", value=12)
action = c3.selectbox("Select operation",["Add","Subtract","Multiply","Divide","Power"])

try:
    result = calculator(num1,num2,action)
    st.success(f"Result: {result}")
except Exception as e:
    st.error(f"Error: {e}")
    
