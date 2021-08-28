from Model.UserInputs import UserInputs as ui
from Model.UserInputs import *

class DerivativeCrossover:

    @staticmethod
    def runDerivativeCrossover():

        # takes derivative of long sma
        ui.df['sma_derivative'] = sym.diff(ui.df['long_sma'])

        # MA for derivative crossover
        print('-------Derivative Plot ------')
        long_dma = int(input('enter long sma length'))
        short_dma = int(input('enter short sma length'))

        # finds 2 moving averages of above
        ui.df['long_sma_derivative'] = ui.df['sma_derivative'].rolling(window=long_dma).mean()
        ui.df['short_sma_derivative'] = ui.df['sma_derivative'].rolling(window=short_dma).mean()

        # visualizes the data from function above
        def dataVisualization():
            # subplots
            fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True,
                                   figsize=(12, 10), gridspec_kw={'height_ratios': [1.5, 1]})
            # subplots
            dv = ax[1]
            price = ax[0]

            # plots the price w/ 2 moving averages
            price.plot(ui.df.index, ui.df['Close'])
            price.plot(ui.df.index, ui.df['short_sma'], color='green', label=f'{ui.short_ma} SMA')
            price.plot(ui.df.index, ui.df['long_sma'], color='red', label=f'{ui.long_ma} SMA')

            # plots derivative moving average
            dv.plot(ui.df.index, ui.df['long_sma_derivative'], color='red', label=f'{long_dma}SMA')
            dv.plot(ui.df.index, ui.df['short_sma_derivative'], color='green', label=f'{short_dma}SMA')
            dv.axhline(y=0)

            price.set_title(f'{ui.ticker.upper()} & Derivative Crossover Chart on {ui.timeframe}')

            # legend
            dv.legend(loc='best')
            price.legend(loc='best')

            plt.show()

        dataVisualization()

    @staticmethod
    def candlestickChart():
        mpf.plot(ui.df, type='candle', style='binance',
                 mav=(ui.short_ma, ui.long_ma), volume=True,
                 title=f'{ui.ticker}, Candlestick Chart {ui.timeframe}')
        plt.show()
