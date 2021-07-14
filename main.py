# Post a Python program that accepts at least two values as input, performs some computation and displays at least one value as the result. The computation must involve calling one of the predefined functions in the math library. Include comments in your program that describe what the program does. Also post a screen shot of executing your program on at least one test case.

# Be sure to choose a program different from any of the programs already posted by your classmates.
import math
# spice
print("ITS CALCULATOR TIME")
#input for which math should be done
Choice = (input("which would would you like to do: \nCOS \nSIN \nTAN \nplease type one \n"))
#input for X value
Xvalue = int(input("Please enter a number: \n"))

#sets up a function to do the math so I can call it later
def Mathstuff():
  #User chooses COS do that else go to the others that they choose
    if Choice == "COS":
      #math import function is being used to get the value
      Xcos = math.cos(Xvalue)
      #prints the output
      print("The COS of {} is {}".format(Xvalue,Xcos))
    elif Choice == "TAN":
      #math import function is being used to get the value  
      Xtan = math.tan(Xvalue)
      print("The TAN of {} is {}".format(Xvalue,Xtan))
    elif Choice == "SIN":
      #math import function is being used to get the value
      Xsin = math.sin(Xvalue)
      print("The SIN of {} is {}".format(Xvalue,Xsin))  



Mathstuff()

