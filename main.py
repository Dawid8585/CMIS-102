# Input NumHoursWorked as float
# Input WeeklySales as float
# Commision = 20% of WeeklySales 
# HourlyPay = 16 
# Totalpay = NumHoursWorked  *  + Commision
# Output”Total hours worked = NumHoursWorked “
# Output”Total commision = Commision “
# Output”Total pay for the week = Totalpay“
# Output Does user want to enter new calculation Yes No
# If No stop
# Else go back to beginning 

play = True

while play:
  while True: 
    try:
    

      #User enters inputs of hours worked and sales #'s.
      NumHoursWorked  = input()
      WeeklySales  = float(input("Enter weekly sales:"))

      # Commision = 20% of WeeklySales 
      CommisionRate = .20
      # HourlyPay = 16$ 
      HourlyPay  = 16
      #Commision is calculated
      Commision  = CommisionRate * WeeklySales

      #Totalpay is calculated
      Totalpay  = NumHoursWorked * HourlyPay + Commision

      #If Hours worked is 0 then you dont get commision or pay
      if NumHoursWorked == 0:
          Commision = 0
          Totalpay = 0
      #Total pay , hours worked, Vommision amount, are displayed to the user, also rounds to the 2nd decimal place
      print('\nTotal hours worked is :',round(NumHoursWorked,2))
      print('\nTotal commision is :',round(Commision,2))
      print('\nTotal pay for the week is :', round(Totalpay,2))
      
      #asks user to restart the program
      PlayAgain=str(input('\nDo you want to enter a new calculation, type Yes or No '))
      #if user writes either no then it stops program
      if PlayAgain == "No":
        play = False
      elif  PlayAgain == "NO":
        play = False  
      break

    # If it fails this will be shown
    except ValueError:
       print("Enter a number, words are not allowed! Try again!")

   

