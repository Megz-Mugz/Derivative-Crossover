import sympy as sym
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
plt.style.use('dark_background')

# user inputs
ticker = input('enter stock ticker')
timeframe = input('enter a timeframe:')
long = int(input('enter length for long SMA (used taken for derivative)'))
short = int(input('enter length for short SMA'))

# load stock data
start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()
df = web.DataReader(ticker, 'yahoo', start, end)

# manipulates stock data
def resample():
    global df
    df = df.resample(timeframe).agg(
                {'Close': 'last',
                 'High': 'max',
                 'Low': 'min',
                 'Open': 'first',
                 'Volume': 'sum'}).dropna()

# computes math for derivative crossover
def setupDC():
    global short, long
    # creates MA for stock chart
    df['long_sma'] = df['Close'].rolling(window=long).mean()
    df['short_sma'] = df['Close'].rolling(window=short).mean()

# runs and visualizes data
class DerivativeCrossover:

    # runs the actual DC
    @staticmethod
    def runDerivativeCrossover():
        global df, long, short

        # takes derivative of long sma
        df['sma_derivative'] = sym.diff(df['long_sma'])

        # MA for derivative crossover
        print('-------Derivative Plot ------')
        long = int(input('enter long sma length'))
        short = int(input('enter short sma length'))

        # finds 2 moving averages of above
        df['long_sma_derivative'] = df['sma_derivative'].rolling(window=long).mean()
        df['short_sma_derivative'] = df['sma_derivative'].rolling(window=short).mean()

        # visualizes the data from function above
        def dataVisualization():
            # subplots
            fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True,
                                   figsize=(12, 10), gridspec_kw={'height_ratios': [1.5, 1]})
            # subplots
            dv = ax[1]
            price = ax[0]

            # plots moving derivative moving average
            dv.plot(df.index, df['long_sma_derivative'], color='red', label=f'{long}SMA')
            dv.plot(df.index, df['short_sma_derivative'], color='green', label=f'{short}SMA')
            dv.axhline(y=0)

            # plots the price w/ 2 moving averages
            price.plot(df.index, df['Close'])
            price.plot(df.index, df['short_sma'], color='green', label=f'{short} SMA')
            price.plot(df.index, df['long_sma'], color='red', label=f'{long} SMA')

            price.set_title(f'{ticker.upper()} & Derivative Crossover Chart on {timeframe}')

            # legend
            dv.legend(loc='best')
            price.legend(loc='best')

            plt.show()
        dataVisualization()

    # visualizes candlesticks
    @staticmethod
    def candlestickChart():
        mpf.plot(df, type='candle', style='nightclouds',
                 mav=(8, 21), volume=True,
                 title=f'{ticker}, Candlestick Chart {timeframe}')

        plt.show()

# asks user a question and uses ternary operator
def user_choice():
    data = input('would you like to see derivative crossover or candlestick chart?(d/c)')
    print(DerivativeCrossover.runDerivativeCrossover() if data.lower() == 'd' else DerivativeCrossover.candlestickChart())

resample()
setupDC()
user_choice()
