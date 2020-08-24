import random
def pattern(wrong, task):
    if (wrong == 0):
        print ("_________")
        print ("|   |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 1):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 2):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|   |")
        print ("|")
        print ("|")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 3):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|   |")
        print ("|   |")
        print ("|")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 4):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|  \|")
        print ("|   |")
        print ("|")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 5):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|  \|/")
        print ("|   |")
        print ("|")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 6):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|  \|/")
        print ("|   |")
        print ("|  /")
        print ("|________")
        print("\n")
        return 1
    elif (wrong == 7):
        print ("_________")
        print ("|   |")
        print ("|   O")
        print ("|  \|/")
        print ("|   |")
        print ("|  / \ ")
        print ("|________")
        print ("\nThe word was ", task)
        print ("\n")
        print ("\nYOU LOSE! TRY AGAIN!")
        again = input("\nWould you like to play again? Y/N")
        if again == "y" or again == "Y":
          hangMan()
        else:
          exit()

def printletter(newstring):
  for y in newstring:
        print(y, end = " ")
  print("\n")
def leng(task):
  count = 0
  duplicates = []
  for x in task:
    if x not in duplicates:
      duplicates.append(x)
      count += 1
  return count
def hangMan():
  words = ["dwarf", "hangman", "prateek", "hate", "nothing", "hell","acres","adult","advice","arrangement","attempt",
"August","Autumn","border","breeze","brick","calm","anal","Casey","cast","chose","claws","coach","constantly","contrast"]
  task = random.choice(words)
  wrong = 0
  newstring = []
  for i in range(len(task)):
    newstring.append("_")
  print("Let's start the game !")
  pattern(wrong, task)
  printletter(newstring)
  print("\n\nGuess a letter : ", end = " ")
  len2 = leng(task)
  condition = 1
  while condition == 1:
    guess = input("\n> ")
    if guess in task:
      for i,x in enumerate(task):
        if guess == x:
          newstring[i] = x
      if "_" in newstring:
        condition = pattern(wrong, task)
        printletter(newstring)
        print("\nGreat work !\nGuess another : ", end = "")
      else:
        condition = pattern(wrong, task)
        printletter(newstring)
        print("Congratulations !")
        print("YOU WIN !")
        again = input("do you want to play again? Y/N : ")
        if again == "y" or again == "Y":
          hangMan()
        else:
          exit()
     
    else:
      wrong += 1
      condition = pattern(wrong, task)
      printletter(newstring)
      print("\nOops...!\nWrong guess.\nGuess another : ", end = "")
      
hangMan() 
  
   
