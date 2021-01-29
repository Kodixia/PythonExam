from portafolioUtileries import Investment

if __name__ == "__main__":
    investor = Investment(5)
    investor.show_assets()
    investor.maxValue([1,2,10])
    investor.show_assets()
    investor.maxValue([2,4,5])
    investor.show_assets()
    investor.maxValue([3,5,12])
    investor.show_assets()