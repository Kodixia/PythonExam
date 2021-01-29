

def priceCheck(products,productsPrices,productSold,soldPrice):
    print("Price")
    print("Product    Actual    Expected    Error")
    for product_sold in range(len(productSold)):
        for product in range(len(products)):
            if(str(productSold[product_sold]) == str(products[product])):
                if soldPrice[product_sold] != productsPrices[product]:
                    print(f"{productSold[product_sold]}        {soldPrice[product_sold]}         {productsPrices[product]}    {1}")
                else:
                    print(f"{productSold[product_sold]}        {soldPrice[product_sold]}         {productsPrices[product]}")


        
