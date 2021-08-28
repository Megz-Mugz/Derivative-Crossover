from Model.UserInputs import UserInputs as ui

class SetupDC:
    @staticmethod
    def setupDC():
        ui.df['long_sma'] = ui.df['Close'].rolling(window=ui.long_ma).mean()
        ui.df['short_sma'] = ui.df['Close'].rolling(window=ui.short_ma).mean()