# The third assignment involves writing a Python program to compute the cost of carpeting a room. Your program should prompt the user for the width and length in feet of the room and the quality of carpet to be used. A choice between three grades of carpeting should be given. You should decide on the price per square foot of the three grades on carpet. Your program must include a function that accepts the length, width, and carpet quality as parameters and returns the cost of carpeting that room. After calling that function, your program should then output the carpeting cost.


# spice
print("Cost of carpeting a room")
#input for width and length should be done
WidthC = float(input("What is the width of the room in feet: "))
LengthC = float(input("\nWhat is the length of the room in feet: "))
#total area of carpet
CarpetArea = WidthC * LengthC
#input for which grade should be done
Choice = float(input("\nWhich grade would would you like to do: \n1:Money Saver: $2.00 sqft \n2:Basic: $5.99 sqft \n3:Bouje Badness: $94.99 sqft\nplease type 1 , 2 or 3 \n"))

#sets up a function to do the math so I can call it later
def Mathstuff():
  #Users choice is evaluated and ran
    if Choice == 1:
      # total price is calculated for the carpet
      TtlPrice = CarpetArea * 2
      #Total price is printed and round to the 2nd decimal point cause money.
      print("Total cost for a basic carpet installation for this room is", round(TtlPrice,2),"$") 
    elif Choice == 2:
      # total price is calculated for the carpet
      TtlPrice = CarpetArea * 5.99
      #Total price is printed and round to the 2nd decimal point cause money.
      print("Total cost for a basic carpet installation for this room is", round(TtlPrice,2),"$") 
    elif Choice == 3:
      # total price is calculated for the carpet
      TtlPrice = CarpetArea * 94.99
      #Total price is printed and round to the 2nd decimal point cause money.
      print("Total cost for a basic carpet installation for this room is", round(TtlPrice,2),"$")
    
#Function is called to do the job
Mathstuff()

