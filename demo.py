from this import c

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
def quad_plot(a,b,c):

    x = np.linspace(-10,10)
    y = a * x ** 2 + b * x + c

    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title("QUADRATIC EQUATION : {a}x^2 + {b}x + {c}")
    st.pyplot(fig)
def main():
    st.title("MATHS VISUALIZATION : QUADRATIC EQUATION")
    st.sidebar.header("QUADRATIC EQUATION COEFFICIENT ")
    a = st.sidebar.slider("COEFFICIENT a", -10,10,0)
    b = st.sidebar.slider("COEFFICIENT b", -10,10,0)
    c = st.sidebar.slider("COEFFICIENT c", -10,10,0)
    quad_plot(a,b,c)
if __name__ == '__main__':
    main()

# terminal - streamlit run demo.py