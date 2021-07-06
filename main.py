import random
while True: 
  try:
    

  #  Welcom message
    print(" ARE YOU READY TO CREATE A CUSTOM POKEMON")
  
    # Input person name
    FirstName  = str(input("\nEnter Your First Name:"))
    MiddleName = str(input("\nEnter Your Middle Name. Enter NA for no middle name: "))
    LastName  = str(input("\nEnter Your Last Name:"))
   
    #if the user inputs NA or na then middle Name is 0 else its the length of the middle name
    if MiddleName == "NA" or "na" or "Na":
      MiddleName = ""

    #gets the level based on the input
    Sec = len(FirstName) + len(LastName) + len(MiddleName)
    first = len(FirstName) + len(LastName) 
    Level = first + len(MiddleName)
    # print("this is", Level)
    # print("this is", first)
    # print("this is", Sec)
    #  List of pokemon Name
    PokemonName = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander","Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie","Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate","Spearow", "Fearow", "Dragonite", "Mewtwo", "Mew"]
    #List of pokemon type
    PokemonType = ["Normal","Fire","Water","Grass","Electric","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dark","Dragon","Steel","Fairy"]   

    #prints out both outputs
    print("Your Pokemon is",  random.choice(PokemonName) ,random.choice(PokemonType) ,"type")
    print("Level:", Level)

    break

    # If it fails this will be shown
  except ValueError:
    print("Enter a word, numbers are not allowed! Try again!")

   

