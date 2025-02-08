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
