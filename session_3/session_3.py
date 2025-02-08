import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go

# Function to load and clean financial data


def load_and_clean_data(file):
    df = pd.read_csv(
        file, parse_dates=["Date"]
    )  # parse_dates converts the "Date" column to datetime format
    for col in ["Open", "High", "Low", "Close"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df.dropna(inplace=True)
    # print(df["Date"].is_unique) # To check if "Date" column is unique
    df.set_index("Date", inplace=True)
    return df


aapl = load_and_clean_data("../session_2/AAPL.csv")
jpm = load_and_clean_data("../session_2/JPM.csv")
msft = load_and_clean_data("../session_2/MSFT.csv")

ohlc_aapl = aapl[["Open", "High", "Low", "Close"]]
ohlc_jpm = jpm[["Open", "High", "Low", "Close"]]
ohlc_msft = msft[["Open", "High", "Low", "Close"]]

mpf.plot(
    ohlc_aapl,
    type="ohlc",
    style="charles",
    title="AAPL OHLC Chart",
    ylabel="Price",
    figscale=3.0,
)

mpf.plot(
    ohlc_aapl,
    type="candle",
    style="charles",
    title="AAPL Candlestick Chart",
    ylabel="Price",
    figscale=3.0,
)

mpf.plot(
    ohlc_jpm,
    type="ohlc",
    style="charles",
    title="JPM OHLC Chart",
    ylabel="Price",
    figscale=3.0,
)

mpf.plot(
    ohlc_jpm,
    type="candlestick",
    style="charles",
    title="JPM Candlestick Chart",
    ylabel="Price",
    figscale=3.0,
)

mpf.plot(
    ohlc_msft,
    type="ohlc",
    style="charles",
    title="MSFT OHLC Chart",
    ylabel="Price",
    figscale=3.0,
)

mpf.plot(
    ohlc_msft,
    type="candlestick",
    style="charles",
    title="MSFT Candlestick Chart",
    ylabel="Price",
    figscale=3.0,
)

# Use Plotly for OHLC and Candlestick Charts
fig = go.Figure()
fig.add_trace(
    go.Ohlc(
        x=aapl.index,
        open=aapl["Open"],
        high=aapl["High"],
        low=aapl["Low"],
        close=aapl["Close"],
        name="AAPl OHLC",
    )
)
fig.update_layout(title="AAPL OHLC", width=2000, height=1000)
fig.show()

fig = go.Figure()
fig.add_trace(
    go.Candlestick(
        x=aapl.index,
        open=aapl["Open"],
        high=aapl["High"],
        low=aapl["Low"],
        close=aapl["Close"],
        name="AAPL Candlestick",
    )
)
fig.update_layout(title="AAPL Candlestick", width=1800, height=1000)
fig.show()

"""
## Homework: Draw charts for JPM and MSFT using Plotly.
Checkout different Financial Charts that exist and try and plot most of them with a writeup of what they represent.
Link: [https://plotly.com/python/financial-charts/](https://plotly.com/python/financial-charts/)
"""


"""
# Advanced Time Series EDA and Techincal Indicator Analysis

In this part, we will learn about Price trend analysis using moving averages, momentum indicators (RSI, MACD), volatility analysis (Bollinger Bands), etc.
"""

import yfinance as yf
import plotly.express as px
import matplotlib.dates as mdates

stocks = ["AMZN", "GOOGL", "TSLA"]

data_dict = {}

for ticker in stocks:
    df = yf.download(ticker, period="3y", interval="1d")
    df.reset_index(inplace=True)
    data_dict[ticker] = df
    print(f"\n{ticker} data (first 10 rows):")
    print(df.head(10))
    print(f"\n{ticker} data (last 10 rows):")
    print(df.tail(10))


# RSI Calculation - Relative Strength Index
def calculate_RSI(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -1 * delta.clip(upper=0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


tesla_df = data_dict["TSLA"]
tesla_df["RSI_14"] = calculate_RSI(df["Close"], period=14)
pd.set_option("display.max_rows", 250)
tesla_df.head(200)
