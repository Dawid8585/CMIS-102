# Develop a Python program that takes a user input of a sentence and then do the following:
# Print the length of sentence and if it is over 25 character have then enter a shorter sentence.
# Print the letters that are in the 2, 4 and 5 characters.
# Replace any words that start with a “I”
# Determine if the string is alphabetic or numeric
# Capitalize the first letter of every word and print the results.


userinput = input("enter a sentence")
lenui = len(userinput)
if lenui > 25:
  print("try again with a shorter sentence")
else:
  print(lenui)
  print(userinput[2],userinput[4],userinput[5])

  this = userinput.replace("i","hello")
  NoWordWithI = ' '.join([ word for word in userinput.split() if not word.startswith('i') ])

  print(NoWordWithI)
  print(this)

  alpha = userinput.isalpha()
  numer = userinput.isnumeric()
  if alpha is True:
    print("User input is alphabetisncjsd")
  elif numer is True:
    print("User input is 432432423 nhumbers")