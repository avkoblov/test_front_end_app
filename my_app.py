import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
barchart = st.container()

@st.cache
def get_data(filename):
    data = pd.read_csv(filename)
    return data

with header:
    st.write('Test app!')

# Using object notation
data = get_data('/Users/Data/data_for_app.csv')
add_asset_name = st.sidebar.selectbox(
    "**SELECT ASSET**",
    (data['asset_name'].unique())
)

# Using "with" notation
with st.sidebar:
    sel_col, disp_col = st.columns(2)
    date_from = sel_col.selectbox('**Date from**', options = data['date'].unique(), index=0)
    date_to = sel_col.selectbox('**Date to**', options = data['date'].unique(), index=0)

with barchart:

    st.bar_chart(data=data.query('date >= @date_from & date <= @date_to & asset_name == @add_asset_name'), x='time', y='priceUsd')
    


