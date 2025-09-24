import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import yfinance as yf
from nicegui import ui

def show_plot():
        pio.renderers.default = "browser"
        fig = go.Figure(data=[go.Candlestick(
                x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close']
        )])

        fig.update_layout(
                title="CandleStick chart of "+t.info['longName'],
                xaxis_title="Data",
                yaxis_title="Price",
                xaxis_rangeslider_visible=True,
                template="plotly_white"
        )

        fig.show()

def fetch(v):
        global t, df
        t = yf.Ticker(v)
        df = t.history("10y")
        df = df.iloc[:, :4]

company = ['ITC.NS', 'RELIANCE.NS', 'TITAN.NS', 'TCS.NS', \
'BHARTIARTL.NS', 'TRENT.NS', 'LT.NS', 'HINDUNILVR.NS', 'HDFCBANK.NS', 'SBIN.NS']
ui.select(company, with_input=True, on_change=lambda e: fetch(e.value))
ui.button('Show plot', on_click=show_plot)
ui.run()
