import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

st.write("""
    # Simple Stock Market Application
    
    Hello, This is my first ever **data science** app 
    
    Shown below are ***stock market*** closing prices of Google!

""")

# define your ticker symbol
ticker_symbol = 'GOOGL'

ticker_Data = yf.Ticker(ticker_symbol)

ticker_df = ticker_Data.history(period='1d', start='2010-05-31', end='2020-05-31')

st.write("## **Closing Price:**")
st.line_chart(ticker_df.Close)

st.write("## **Volume Price:**")
st.line_chart(ticker_df.Volume)

