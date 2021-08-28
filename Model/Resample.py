from Model.UserInputs import UserInputs

class Resample:
    @staticmethod
    def resample():
        df = UserInputs.df.resample(UserInputs.timeframe).agg(
            {'Close': 'last',
             'High': 'max',
             'Low': 'min',
             'Open': 'first',
             'Volume': 'sum'}).dropna()