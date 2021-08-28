import sympy as sym
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
plt.style.use('dark_background')

class UserInputs:
    # user inputs
    ticker = input('enter stock ticker')
    print(mpf.available_styles())
    timeframe = input('enter a timeframe:')
    long_ma = int(input('enter length for long SMA (used taken for derivative)'))
    short_ma = int(input('enter length for short SMA'))

    # load stock data
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime.now()
    df = web.DataReader(ticker, 'yahoo', start, end)