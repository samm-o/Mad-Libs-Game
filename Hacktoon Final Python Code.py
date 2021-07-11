import os
import sys
import time

class item:
    name = ""
    description = ""
    quantity = None

    def __init__(self, iName, iDescription, iQnt):
        self.name = iName
        self.description = iDescription
        self.quantity = iQnt

    def prtItem(self):
        print(self.name, self.description, self.quantity)

#function Definitions

#Part 1 Functions


#Menu Funtions
def mainMenu():
    prtHeader(" Mad Libs ")
    cont = False
    options = (1,2,9) 
    while not cont:

      num = input("Please select an Option\n1. Start\n2. Help\n9. Exit\n")
      if ValidateInt(num, options):
        num = int(num)
        cont = True
      else:
        os.system('cls')
        print("Invalid input")

    return num

def Start(): 
  os.system('cls')
  prtHeader(" Mad Libs Stories! ")
  v1 = item("1. Summer Vacation!", "", "")
  v2 = item("2. The Superkid!", "", "")
  v3 = item("3. Starwars!", "", "")
  stories = [v1, v2, v3]
  print("These are the stories we have: \n")
  print("".center(50,"-"))
  printList(stories)
  print("".center(50,"-"))

def selectionstory():

  story_selection = input("What is the item number of your selection?")
  if (story_selection.isdigit() == False):
    os.system('cls')
    print("You have selected an invalid option, relaunch the program to retry. BYE BYE")
    time.sleep(3)
    sys.exit()
  else:

    story_selection = int(story_selection)

    if (story_selection == 1):
      var1 = input("Please type in an adjective! ")
      var2 = input("Please type in an adjective! ")
      var3 = input("Please type in a noun! ")
      var4 = input("Please type in a noun! ")
      var5 = input("Please type in a plural noun! ")
      var6 = input("Please type in a game! ")
      var7 = input("Please type in a plural noun! ")
      var8 = input("Please type in a VERB ENDING IN “ING”! ")
      var9 = input("Please type in a VERB ENDING IN “ING”! ")
      var10 = input("Please type in a plural noun! ")
      var11 = input("Please type in a VERB ENDING IN “ING”! ")
      var12 = input("Please type in a NOUN! ")
      var13 = input("Please type in a plant! ")
      var14 = input("Please type in a part of the body! ")
      var15 = input("Please type in a place! ")
      var16 = input("Please type in a VERB ENDING IN “ING”! ")
      var17 = input("Please type in an adjective! ")
      var18 = input("Please type in a number! ")
      var19 = input("Please type in a plural noun! ")
      
      os.system('cls')
      print("Creating Story!")
      time.sleep(2)
      
      os.system('cls')
      story_1 = ("A vacation is when you take a trip to some " + var1 +" place with your "+ var2 +" family. Usually you go to some place that is near a/an "+ var3 +" or up on a/an "+ var4 + ". A good vacation place is one where you can ride "+ var5 +" or play "+ var6 +" or go hunting for "+ var7 +". I like to spend my time "+ var8 +" or "+ var9 +". When parents go on a vacation, they spend their time eating three "+ var10 +" a day, and fathers play golf, and mothers sit around "+ var11 +". Last summer, my little brother fell in a/an "+ var12 + " and got poison "+ var13 +" all over his "+ var14 +". My family is going to go to (the) "+ var15+ " and I will practice "+ var16 +". Parents need vacations more than kids because parents are always very "+ var17 +" and because they have to work "+ var18 +" hours every day all year making enough "+ var19 +" to pay for the vacation.")

      
      print(story_1)
      time.sleep(5)
      
    elif (story_selection == 2):
      lar1 = input("Please type in your name! ")
      lar2 = input("Please type in a noun! ")
      lar3 = input("Please type in a name ")
      lar4 = input("Please type in a verb! ")
      lar5 = input("Please type in a name! ")
      lar6 = input("Please type in a color! ")
      lar7 = input("Please type in a noun! ")
      lar8 = input("Please type in a city! ")
      lar9 = input("Please type in a verb! ")
      lar10 = input("Please type in a verb! ")
      lar11 = input("Please type in a verb! ")
      lar12 = input("Please type in a noun! ")
      lar13 = input("Please type in a food! ")
      lar14 = input("Please type in a name of a school! ")

      os.system('cls')
      print("Creating Story!")
      time.sleep(2)
      
      os.system('cls')

      story_2 = ("Hi! My name is "+lar1+" and I have a secret to share with you. I'm a normal child by day, and a "+lar2+" by night. Only you and my best friend, "+lar3+" know my secret. You may be wondering how this happened? Well, one night I was "+lar4+" at home, and then BOOM! The lights went out and "+lar5+" showed up. He/she said in a booming voice, because your favorite color is "+lar6+" you have been chosen to be a "+lar7+". My mission is to save the people of "+lar8+" by doing my favorite things: "+lar9+", "+lar10+", and "+lar11+". This may sound easy, it is no walk in the park. It requires hard work and "+lar12+". My weakness is eating" +lar13+ ". They are gross!! Keep that away from me! I save the world every night But when I wake up in the morning, I go back to my normal life at "+lar14+" School!")

      print(story_2)
      time.sleep(5)

    elif (story_selection == 3):
      far1 = input("Please type in adjective! ")
      far2 = input("Please type in a noun! ")
      far3 = input("Please type in a adjective! ")
      far4 = input("Please type in a place! ")
      far5 = input("Please type in a adjective! ")
      far6 = input("Please type in a adjective! ")
      far7 = input("Please type in a plural noun;vehicle! ")
      far8 = input("Please type in a adjective! ")
      far9 = input("Please type in a adjective! ")
      far10 = input("Please type in a plural noun! ")
      far11 = input("Please type in a adjective! ")
      far12 = input("Please type in a plural noun! ")
      far13 = input("Please type in a plural noun! ")
      far14 = input("Please type in an adjective! ")
      far15 = input("Please type in a noun! ")
      far16 = input("Please type in a verb! ")
      far17 = input("Please type in an adjective! ")
      far18 = input("Please type in a verb! ")
      far19 = input("Please type in a plural noun! ")
      far20 = input("Please type in a plural noun;type of job! ")
      far21 = input("Please type in a adjective! ")
      far22 = input("Please type in a verb! ")
      far23 = input("Please type in a adjective! ")

      os.system('cls')
      print("Creating Story!")
      time.sleep(2)
      
      os.system('cls')

      story_3 = ("Star Wars is a "+ far1+" "+ far2+ " of "+far3+ " versus evil in a " +far4+" far far away. There are " + far5 + " battles between " + far6 +" "+ far7 +" in " + far8 + " space and " + far9 + " duels with " + far10 + " called "+far11+" sabers. " + far12+ " called droids are helpers and " +far13+ " to the heroes. A "+far14+" power called The " +far15+" "+far16+" "+"s people to do "+far17+" things, like "+far18+" "+far19++". The Jedi "+far20+" use The Force for the "+far21+" side and the Sith "+far22+ " it for the "+far23+" side.")
      
      print(story_3)
      time.sleep(5)


    else:
      os.system('cls')
      print("You have selected an invalid option, relaunch the program to retry. BYE BYE")
      time.sleep(3)
      sys.exit()

def Help():
  prtHeader(" Help Guide ")
  h1 = item("1. How to Play", " ", " ") 
  h2 = item("2. Return", " ", " ")   
  help_options = [h1, h2]
  print("".center(50,"-"))
  printList(help_options)
  print("".center(50,"-"))

def selectionhelp():

  help_selection = input("What is the item number of your selection? ")
  help_selection = int(help_selection)

  if (help_selection == 1):
    os.system('cls')
    print("\nThe mad libs game is a very fun game to play with friends and family. Simply click start and choose a Mad libs story of your choice! Next it will ask you to type in different categories of words e.g (Nouns, Adjectives, Verbs, etc.) It will then fill in your words with the story and make a hilarious story that your friends and family will enjoy!\n")
    time.sleep(5)
	
  elif (help_selection == 2):
    time.sleep(1)
    os.system('cls')

  elif (help_selection > 2 or help_selection < 1):
    print("You have selected an invalid option, relaunch the program to retry. BYE BYE")
    os.system('cls')
    sys.exit()

#Helper Functions
#Functions for Printing lists, 

def ValidateYorN(entry):
  result = False
  if entry.lower() == "y" or entry.lower() == "n":   
      result = True
  return result

def ValidateInt(entry, values):
  result = False
  if entry.isdigit():
    if int(entry) in values:
      result = True
  return result

def printList(items):
  for item in items:
    item.prtItem()
        
def prtHeader(strHeader):
  print("".center(50,"#"))
  print(strHeader.center(50,"@"))
  print("".center(50,"#"))


#Main Menu code (when selecting either Start, help or exit, list will appear)
while True:
    selection = mainMenu()
    os.system('cls')
    if selection == 1:
        os.system('cls')
        Start()
        selectionstory()
        read = input("\nType 'y' when you have read the MADLIB: ")
        if read == 'y':
          os.system('cls')
          print("Thank you for playing our Mad Libs Game! If you enjoyed it please give us some support on Github: samm-o & ArnavDalmia")
          print("\nThis Program will close in 5 Seconds.")
          time.sleep(6)
          sys.exit()
        else:
          os.system('cls')
          print("You have selected an Invalid Option. Please relaunch the program")
          time.sleep(2)
          sys.exit
    elif selection == 2:
        Help()
        selectionhelp()
    elif selection == 9:
        cont = False
        confirm = False
        while not cont:
            print("Thank you for playing our Mad Libs Game! If you enjoyed it please give us some support on Github: samm-o & ArnavDalmia\n\nAre you sure you want to exit our amazing game?! (y/n)")
            YN = input()
            if ValidateYorN(YN):  
                cont = True
            if YN.lower() == 'y':
                confirm = False
                os.system('cls')
                print("This Program will close in 1 second")
                time.sleep(2)
                os.system('cls')
                sys.exit()
            elif YN.lower() == 'n':
                confirm = True
                os.system('cls')
                input("\nPress Enter to return to the previous menu")
                os.system('cls')
            else:
                confirm = True
                print("You have selected an invalid input. Please relaunch the program.")
                time.sleep(6)
                os.system('cls')
                sys.exit()
