actual_cost = (float(input("Enter the actual cost of the product:")))
selling_price = (float(input("Enter the selling price of the product:")))

if (selling_price > actual_cost):
    amount = selling_price - actual_cost
    print("Total profit =", amount)

else :
    print("No profit!!!")