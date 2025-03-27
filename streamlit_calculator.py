import streamlit as st
import math
import numpy as np

# Set page config
st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 50px;
        margin: 2px;
        font-size: 20px;
        border-radius: 10px;
        background-color: #2b2b2b;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #3b3b3b;
    }
    .calculator-display {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: right;
        font-size: 32px;
        color: white;
        min-height: 80px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for calculator
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'memory' not in st.session_state:
    st.session_state.memory = 0

# Title
st.title("Scientific Calculator")

# Display
st.markdown(f'<div class="calculator-display">{st.session_state.display}</div>', unsafe_allow_html=True)

# Calculator functions
def add_to_display(value):
    st.session_state.display += value

def clear():
    st.session_state.display = ""

def backspace():
    st.session_state.display = st.session_state.display[:-1]

def calculate():
    try:
        result = eval(st.session_state.display)
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

def sin():
    try:
        value = float(st.session_state.display)
        result = math.sin(math.radians(value))
        st.session_state.display = str(round(result, 6))
    except:
        st.session_state.display = "Error"

def cos():
    try:
        value = float(st.session_state.display)
        result = math.cos(math.radians(value))
        st.session_state.display = str(round(result, 6))
    except:
        st.session_state.display = "Error"

def tan():
    try:
        value = float(st.session_state.display)
        result = math.tan(math.radians(value))
        st.session_state.display = str(round(result, 6))
    except:
        st.session_state.display = "Error"

def sqrt():
    try:
        value = float(st.session_state.display)
        result = math.sqrt(value)
        st.session_state.display = str(round(result, 6))
    except:
        st.session_state.display = "Error"

def square():
    try:
        value = float(st.session_state.display)
        result = value ** 2
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

def cube():
    try:
        value = float(st.session_state.display)
        result = value ** 3
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

def log():
    try:
        value = float(st.session_state.display)
        result = math.log10(value)
        st.session_state.display = str(round(result, 6))
    except:
        st.session_state.display = "Error"

def ln():
    try:
        value = float(st.session_state.display)
        result = math.log(value)
        st.session_state.display = str(round(result, 6))
    except:
        st.session_state.display = "Error"

def memory_clear():
    st.session_state.memory = 0

def memory_recall():
    st.session_state.display = str(st.session_state.memory)

def memory_add():
    try:
        value = float(st.session_state.display)
        st.session_state.memory += value
        st.session_state.display = ""
    except:
        st.session_state.display = "Error"

def memory_subtract():
    try:
        value = float(st.session_state.display)
        st.session_state.memory -= value
        st.session_state.display = ""
    except:
        st.session_state.display = "Error"

# Create columns for the calculator layout
col1, col2, col3, col4 = st.columns(4)

# Scientific functions
with col1:
    st.button("sin", key="sin", on_click=sin)
    st.button("x²", key="square", on_click=square)
    st.button("π", key="pi", on_click=lambda: add_to_display(str(math.pi)))
    st.button("C", key="clear", on_click=clear)
    st.button("⌫", key="backspace", on_click=backspace)
    st.button("±", key="toggle_sign", on_click=lambda: add_to_display("-"))
    st.button("MR", key="memory_recall", on_click=memory_recall)
    st.button("7", key="7", on_click=lambda: add_to_display("7"))
    st.button("4", key="4", on_click=lambda: add_to_display("4"))
    st.button("1", key="1", on_click=lambda: add_to_display("1"))
    st.button("0", key="0", on_click=lambda: add_to_display("0"))

# Numbers and operations
with col2:
    st.button("cos", key="cos", on_click=cos)
    st.button("x³", key="cube", on_click=cube)
    st.button("e", key="e", on_click=lambda: add_to_display(str(math.e)))
    #st.button("<x", key="backspace", on_click=backspace)
    st.button("±", key="toggle_sign", on_click=lambda: add_to_display("-"))
    st.button("M+", key="memory_add", on_click=memory_add)
    st.button("8", key="8", on_click=lambda: add_to_display("8"))
    st.button("5", key="5", on_click=lambda: add_to_display("5"))
    st.button("2", key="2", on_click=lambda: add_to_display("2"))
    st.button(".", key="decimal", on_click=lambda: add_to_display("."))

with col3:
    st.button("tan", key="tan", on_click=tan)
    st.button("log", key="log", on_click=log)
    st.button("(", key="open_paren", on_click=lambda: add_to_display("("))
    st.button("±", key="toggle_sign", on_click=lambda: add_to_display("-"))
    st.button("M-", key="memory_subtract", on_click=memory_subtract)
    st.button("9", key="9", on_click=lambda: add_to_display("9"))
    st.button("6", key="6", on_click=lambda: add_to_display("6"))
    st.button("3", key="3", on_click=lambda: add_to_display("3"))
    st.button("=", key="equals", on_click=calculate)    
with col4:
    st.button("√", key="sqrt", on_click=sqrt)
    st.button("ln", key="ln", on_click=ln)
    st.button(")", key="close_paren", on_click=lambda: add_to_display(")"))
    st.button("MC", key="memory_clear", on_click=memory_clear)
    st.button("/", key="divide", on_click=lambda: add_to_display("/"))
    st.button("*", key="multiply", on_click=lambda: add_to_display("*"))
    st.button("-", key="subtract", on_click=lambda: add_to_display("-"))
    st.button("+", key="add", on_click=lambda: add_to_display("+"))
# Add instructions
st.markdown("""
    ### Instructions:
    1. Use the number pad (0-9) to input numbers
    2. Use operation buttons (+, -, *, /) for basic arithmetic
    3. Use scientific functions (sin, cos, tan, log, etc.)
    4. Use memory functions (MC, MR, M+, M-)
    5. Press "=" to calculate results
    6. Press "C" to clear the display
    7. Press "⌫" for backspace
    8. Press "±" to toggle between positive and negative numbers
    
    Note: Trigonometric functions (sin, cos, tan) work with degrees.
""") 
