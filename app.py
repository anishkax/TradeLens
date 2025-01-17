import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go  
import pandas as pd

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.set_page_config(page_title="TRADELENS", page_icon="📉", layout="centered")

st.markdown("<h3 style='text-align: center; color: #4CAF50; font-size: 40px;'>Stock Prediction App</h3>", unsafe_allow_html=True)

st.markdown(""" 
    <style>
        .dropdown-container {
            margin: 30px;
            padding: 15px;
            background-color: #f1f1f1;
            border-radius: 10px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            width: 100%;
        }

        .dropdown-button {
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border: none;
            border-radius: 10px;
            width: 100%;
            font-size: 20px;
            cursor: pointer;
        }

        .dropdown-content {
            display: none;
            background-color: #f9f9f9;
            min-width: 250px;
            border: 1px solid #ddd;
            border-radius: 10px;
            position: absolute;
            z-index: 1;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }

        .dropdown-container:hover .dropdown-content {
            display: block;
        }

        .dropdown-item {
            padding: 12px 20px;
            font-size: 18px;
            text-decoration: none;
            color: black;
            display: block;
            border-bottom: 1px solid #ddd;
        }

        .dropdown-item:hover {
            background-color: #ddd;
        }

        .streamlit-expanderHeader {
            font-size: 25px !important;
        }

        .streamlit-expanderContent {
            font-size: 18px;
        }

        .stButton>button {
            font-size: 20px;
            padding: 12px 24px;
        }

        .stSlider>div>label {
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="dropdown-container">
        <button class="dropdown-button">Select Stock Dataset</button>
        <div class="dropdown-content">
            <a class="dropdown-item" href="#">AAPL</a>
            <a class="dropdown-item" href="#">GOOG</a>
            <a class="dropdown-item" href="#">MSFT</a>
            <a class="dropdown-item" href="#">GME</a>
            <a class="dropdown-item" href="#">NVDA</a>
            <a class="dropdown-item" href="#">TSLA</a>
            <a class="dropdown-item" href="#">BTC-USD</a>
            <a class="dropdown-item" href="#">ETH-USD</a>
            <a class="dropdown-item" href="#">META</a>
            <a class="dropdown-item" href="#">JPM</a>
            <a class="dropdown-item" href="#">AMZN</a>
        </div>
    </div>
""", unsafe_allow_html=True)

stocks = ("AAPL", "GOOG", "MSFT", "GME", "NVDA", "TSLA", "BTC-USD", "ETH-USD", "META", "JPM", "AMZN")
selected_stocks = st.selectbox("Select stock:", stocks)

n_years = st.slider("Prediction years:", 1, 4, key='slider', help="Select years to forecast.")
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data...done!")

st.subheader("Raw Data", anchor="raw-data")
st.write(data.tail())

def plot_raw_data():
    st.markdown("#### Time Series Data")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock Open', line=dict(color='#1f77b4')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close', line=dict(color='#ff7f0e')))
    fig.update_layout(title_text="Stock Prices Over Time", xaxis_rangeslider_visible=True,
                      plot_bgcolor="#f9f9f9", title_font=dict(size=15, color="black"),
                      font=dict(color="black"), height=500, width=850)
    st.plotly_chart(fig, use_container_width=False)

plot_raw_data()

with st.expander("Click here to view Forecasting Results"):
    if 'Close' in data.columns:
        df_train = data[['Date', 'Close']].dropna()
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)

        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        st.subheader("Forecast Data")
        st.write(forecast.tail())

        st.markdown("#### Forecast Plot")
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1, use_container_width=False, height=500, width=850)

        st.markdown("#### Forecast Components")
        fig2 = m.plot_components(forecast)
        st.pyplot(fig2, clear_figure=True)
    else:
        st.error("The 'Close' column is missing in the data.")
