from Model.DerivativeCrossover import *

class UserChoice:
    @staticmethod
    def user_choice():
        data = input('would you like to see derivative crossover or candlestick chart?(d/c)')
        print(DerivativeCrossover.runDerivativeCrossover() if data.lower() == 'd' else DerivativeCrossover.candlestickChart())