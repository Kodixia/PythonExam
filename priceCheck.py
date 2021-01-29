from priceCheckUtileries import priceCheck

if __name__ == "__main__":
    products = ["eggs","milk","cheese"]
    productsPrices = [2.89,3.29,5.79]
    productSold = ['eggs','eggs','cheese','milk']
    soldPrice = [2.89,2.99,5.97,3.29]
    priceCheck(products,productsPrices,productSold,soldPrice)
    