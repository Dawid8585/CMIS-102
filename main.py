while True: 
  try:
    

   
    print("\n Ticket Prices are: \n Student Ticket: $25 \n Regular Ticket: $35 \n Senior Ticket is $20")

    AgeClient  = int(input("\nEnter the age of person buying ticket:"))
   
    StudentTicket = 25
    SeniorTicket = 20
    RegularTicket = 35

   

    if AgeClient < 18:
      print("Individual can not purchase ticket")
    elif AgeClient >= 18 and AgeClient <= 25:
      print("Student ticket price is $", StudentTicket) 
    elif AgeClient > 60:
      print("Senior ticket price is $", SeniorTicket)
    elif AgeClient >= 26 and AgeClient <= 60:
      print("Regular ticket price is $", RegularTicket)
   
    
    break

    # If it fails this will be shown
  except ValueError:
    print("Enter a number, words are not allowed! Try again!")

   

