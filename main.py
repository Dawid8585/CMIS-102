# The sixth assignment involves writing a Python program to read in the temperatures, as user input, for ten consecutive days in Celsius and store them into an array. The entire array should then be displayed. Next each temperature in the array should be converted to Fahrenheit and the entire array should be again be displayed. The formula for converting Celsius to Fahrenheit is °F = (°C × 1.8) + 32. Finally, the number of cool, warm and hot days should be counted and the number of each type of days should be displayed. You should decide on the thresholds for determining whether a day is cool, warm or hot..

#grabs the input of the number of days and sets default arrays and values
NumInput = int(input("Number of days: "))
CTemp = []
FTemp =[]
CDays = NumInput
FDays = NumInput

#when the inputed days is equal or more than 1 as for the temp
while NumInput >= 1:
  intemp = int(input("What is temp in Celsius for day {}:  ".format(NumInput) ))
  NumInput -= 1
  #add the temp into the array
  CTemp.append(intemp)

#do calc for turing Cel into Farn
for x in CTemp:
  FarT = (x * 1.8) + 32
  FTemp.append(FarT)
  
#display Celcius and day 
for x in CTemp:
  print("The Celcius on day {} was: {}".format(CDays,x))
  CDays -= 1

#display Fahrenheit and day 
for x in FTemp:
  print("The Fahrenheit on day {} was: {}".format(FDays,x))
  FDays -= 1