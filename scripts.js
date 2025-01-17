document.getElementById("buy-button").addEventListener("click", () => {
    alert("You clicked Buy.");
});

document.getElementById("sell-button").addEventListener("click", () => {
    alert("You clicked Sell.");
});

document.getElementById("forecast-button").addEventListener("click", () => {
    alert("You clicked Forecast. Implement backend forecasting logic.");
});

// Plotting stock chart
function plotStockChart() {
    var data = {
        x: ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01'],
        y: [150, 155, 160, 158],
        type: 'scatter',
        mode: 'lines+markers',
        name: 'AAPL Stock Price'
    };

    var layout = {
        title: 'AAPL Stock Price Over Time',
        xaxis: { title: 'Date' },
        yaxis: { title: 'Price ($)' },
        plot_bgcolor: '#f4f4f4',
        paper_bgcolor: 'white',
    };

    Plotly.newPlot('chart-container', [data], layout);
}

plotStockChart();
