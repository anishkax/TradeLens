# Stock Forecasting Model with News Factor Analysis  

This project aims to develop an intuitive and accurate stock forecasting model that integrates a news factor analysis framework for better interpretability. By analyzing historical stock data for 10 companies over the past five years, the model generates precise forecasts, detailed visualizations, and component breakdowns. Users can make predictions for time horizons ranging from 1 to 4 years, gaining valuable insights into stock trends.  

## Key Features  

- **Reliable Stock Forecasting:** Uses the Prophet model to predict future trends.  
- **Interactive Visualizations:** Displays historical and forecasted stock data with Plotly.  
- **Optimized Performance:** Implements a caching mechanism to reduce redundant API requests.  
- **User-Friendly Interface:** Built with Streamlit for a clean, modern, and responsive experience.  
- **Scalable Deployment:** Designed for cloud hosting to ensure easy accessibility.  

## Workflow Overview  

### 1. Data Collection  
- Retrieves historical stock data using the `yfinance` library.  
- Implements caching to minimize redundant API calls and improve performance.  

### 2. Data Processing  
- Cleans and standardizes data to ensure compatibility with the Prophet forecasting model.  
- Handles missing values and resolves inconsistencies for reliable predictions.  

### 3. Frontend Development  
- Designed with HTML, CSS, and Streamlit for a professional and responsive UI.  
- Includes dropdown menus, sliders, and expandable sections for an intuitive user experience.  

### 4. Data Visualization  
- Uses Plotly to create interactive time-series charts for stock trends.  
- Breaks down forecasts into key components like trend and seasonality for deeper insights.  

### 5. Forecasting  
- Leverages the Prophet model to generate accurate stock price predictions.  
- Automates future date frame creation based on user-defined forecast periods.  

### 6. Deployment  
- Undergoes rigorous testing to ensure stability, accuracy, and ease of use.  
- Prepares for cloud hosting to enable seamless access for users.  

## Technologies Used  

- **Programming Language:** Python  
- **Data Source:** Yahoo Finance API (`yfinance`)  
- **Forecasting Model:** Prophet  
- **Visualization:** Plotly  
- **Frontend:** Streamlit  
- **Data Processing:** Pandas & NumPy  

## Contributing  

Contributions are welcome. If you have ideas for improvements, feel free to submit an issue or a pull request.  

## License  

This project is licensed under the MIT License.
