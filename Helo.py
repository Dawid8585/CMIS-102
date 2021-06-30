while True:
  try:

    #User enters revenue and cost.
    revenue = float(input("Enter the Total Revenue of store: "))
    cost = float(input("Enter the Total Cost of store:"))

    #Profit is calculated
    Profit = revenue - cost
    
    #Profit is displayed
    print('Store profit is: $',Profit)

    break
  except ValueError:
      print("Enter a number words are not allowed! Try again!")