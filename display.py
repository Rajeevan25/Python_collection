import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

import graphviz as graphviz

rand=np.random.normal(3, 2, size=20) # generates an array of 20 random numbers using NumPy's random.normal() function with a mean of 1 and a standard deviation of 2.
fig, ax = plt.subplots()
ax.hist(rand, bins=10)  # bin number of regions
st.pyplot(fig)

df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)

#df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.bar_chart(df)

#df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)


st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)