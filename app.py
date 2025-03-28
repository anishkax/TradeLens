import streamlit as st
from datetime import date
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from prophet.plot import plot_plotly


# Constants
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.set_page_config(page_title="TRADELENS", page_icon="📉", layout="centered")

st.markdown("<h3 style='text-align: center; color: #white;'>Tradelens tock Prediction</h3>", unsafe_allow_html=True)

stocks = ("AAPL", "GOOG", "MSFT", "GME", "NVDA", "TSLA", "META", "JPM", "AMZN", "BTC-USD", "ETH-USD")
selected_stock = st.selectbox("Select Stock:", stocks)

n_years = st.slider("Prediction Years:", 1, 7)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, _ = ts.get_daily(symbol=ticker, outputsize='full')
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

if data is None or data.empty:
    st.error("No data available for the selected stock. Please try again later.")
else:
    st.subheader("Raw Data")
    
    min_date, max_date = st.slider(
        "Filter by Date Range:",
        min_value=pd.to_datetime(data['date']).min().date(),
        max_value=pd.to_datetime(data['date']).max().date(),
        value=(pd.to_datetime(data['date']).min().date(), pd.to_datetime(data['date']).max().date())
    )
    
    filtered_data = data[(pd.to_datetime(data['date']).dt.date >= min_date) & (pd.to_datetime(data['date']).dt.date <= max_date)]
    st.write(filtered_data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=filtered_data['date'], y=filtered_data['1. open'], name='Stock Open', line=dict(color='#1f77b4')))
        fig.add_trace(go.Scatter(x=filtered_data['date'], y=filtered_data['4. close'], name='Stock Close', line=dict(color='#ff7f0e')))
        fig.update_layout(title="Stock Prices Over Time", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()

    def plot_volume_and_high_low():
        fig = go.Figure()
        fig.add_trace(go.Bar(x=filtered_data['date'], y=filtered_data['5. volume'], name='Volume', marker=dict(color='#17becf')))
        fig.add_trace(go.Scatter(x=filtered_data['date'], y=filtered_data['2. high'], name='High Price', line=dict(color='#2ca02c')))
        fig.add_trace(go.Scatter(x=filtered_data['date'], y=filtered_data['3. low'], name='Low Price', line=dict(color='#d62728')))
        fig.update_layout(title="Volume and High/Low Prices Over Time", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_volume_and_high_low()

    with st.expander("View Forecasting Results"):
        df_train = filtered_data[['date', '4. close']].copy()
        df_train.rename(columns={"date": "ds", "4. close": "y"}, inplace=True)
        df_train['y'] = pd.to_numeric(df_train['y'], errors='coerce')
        df_train.dropna(inplace=True)

        if df_train.shape[0] < 2:
            st.error("Not enough valid data available for forecasting.")
        else:
            m = Prophet()
            m.fit(df_train)

            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            st.subheader("Forecast Data")
            st.write(forecast.tail())

            st.markdown("#### Forecast Plot")
            fig1 = plot_plotly(m, forecast)
            st.plotly_chart(fig1)

            st.markdown("#### Forecast Components")
            fig2 = m.plot_components(forecast)
            st.pyplot(fig2, clear_figure=True)
