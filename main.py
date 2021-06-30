
while True: 
  try:
    

    #User enters inputs of test scores
    FirstTest  = float(input("Enter the first Test score:"))
    SecondTest  = float(input("Enter seconf test score :"))
  
    #Total is calculated
    Total = FirstTest + SecondTest
    
    Avg = Total/2

    #Avg grade is displayed and rounded to the 2nd decimal
    print('\n The avg grade is:', round(Avg,2))
    break
    # If it fails this will be shown
  except ValueError:
    print("Enter a number, words are not allowed! Try again!")

   

