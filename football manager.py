import random
import time
import os
import sys

#clear function
def clear():
  os.system('cls||clear')

# defender name, position, rating
defenderName = ['A.Ramos', 'B.Silva', 'W.He', 'C.Lopez', 'D.Kim', 'E.Sanchez', 'F.Nguyen', 'G.Patel', 'S.Miller', 'H.Lee', 'J.Chen', 'I.Wang', 'L.Stone', 'P.Roberts', 'D.Johnson', 'J.Garcia', 'F.Anderson', 'K.Singh', 'L.Murphy', 'C.Mitchell', 'M.Jensen', 'M.Kante', 'J.Walker', 'N.Olsen', 'O.Thompson', 'N.Harris', 'P.Williams', 'Q.Quansah', 'M.Das', 'L.Parker', 'R.Johnson', 'R.Wright', 'S.Zhang', 'T.Martinez', 'T.White', 'U.Khan', 'V.Ibrahim', 'M.Thompson', 'W.Thomas', 'X.Gonzalez', 'Y.Mbappe', 'Z.Fernandes', 'A.Lopez', 'E.Martin', 'B.Kim', 'S.Baker', 'C.Lee', 'D.James', 'E.Gomez', 'F.Murphy']
defenderCountry = ['Spain', 'Portugal', 'China', 'Mexico', 'South Korea', 'Argentina', 'Vietnam', 'India', 'England', 'South Korea', 'China', 'China', 'England', 'Chile', 'England', 'Mexico', 'South Korea', 'India', 'Ireland', 'Sweden', 'Denmark', 'Ethiopia', 'Italy', 'Denmark', 'Australia', 'Argentina', 'Australia', 'Czech Republic', 'India', 'Greece', 'USA', 'Netherlands', 'China', 'Argentina', 'Canada', 'Pakistan', 'Sweden', 'Egypt', 'England', 'Mexico', 'France', 'Czech Republic', 'Spain', 'Spain', 'South Korea', 'Russia', 'South Korea', 'Jamaica', 'Argentina', 'Ireland']
defenderRating = ['93', '92', '91', '89', '88', '86', '84', '83', '82', '82', '81', '81', '80', '80', '79', '79', '78', '78', '77', '76', '76', '75', '75', '75', '74', '73', '73', '72', '71', '71', '69', '69', '69', '68', '68', '67', '66', '66', '66', '66', '65', '64', '63', '62', '62', '61', '61', '60', '60', '60']

# midfielder name, position, rating
midfielderName = ['M.Zacharia', 'P.Gomez', 'R.Lopez', 'S.Romero', 'T.Silva', 'L.Son', 'U.Hernandez', 'V.Nguyen', 'D.Bolton', 'W.Patel', 'M.Smith', 'A.Ayalew', 'M.Brown', 'X.Kim', 'Q.Andrews', 'Y.Zhang', 'Z.Lee', 'A.Ng', 'M.Davis', 'B.Ochoa', 'W.Thomas', 'CC.Khan', 'L.Moss', 'L.Williams', 'D.Smith', 'S.Steven', 'M.Jones', 'J.Wilson', 'E.Martinez', 'M.Garcia', 'F.Diaz', 'Y.Miller', 'G.Tran', 'H.Santos', 'M.Yousef', 'I.Jackson', 'J.Sharma', 'K.Mbappe', 'L.Hammersmith', 'O.Anderson', 'M.Johnson', 'N.Garcia', 'O.Ibrahim', 'P.Thomas', 'Q.Williams', 'R.Star', 'S.Taylor', 'T.Miller']
midfielderCountry = ['India', 'Argentina', 'Spain', 'Italy', 'Portugal', 'South Korea', 'Mexico', 'Vietnam', 'England', 'India', 'China', 'Ghana', 'Sweden', 'South Korea', 'Scotland', 'China', 'South Korea', 'Singapore', 'France', 'Mexico', 'England', 'Pakistan', 'England', 'England', 'Jamaica', 'England', 'France', 'Saudi Arabia', 'Chile', 'Germany', 'Chile', 'Senegal', 'Vietnam', 'Brazil', 'Egypt', 'Canada', 'India', 'France', 'Czech Republic', 'India', 'USA', 'Mexico', 'Sweden', 'England', 'Australia', 'Poland', 'Germany', 'Canada']
midfielderRating = ['94', '93', '92', '89', '88', '86', '85', '84', '83', '82', '81', '80', '79', '79', '78', '78', '77', '76', '75', '75', '74', '74', '73', '73', '73', '72', '72','69', '68', '68', '68', '67', '67', '67', '67', '66', '66', '66', '66', '65', '65', '64', '63', '62', '61', '60', '60', '60']

# attacker name, position, rating
attackerName = ['A.Rodriguez', 'B.Hernandez', 'J.Edwards', 'C.Zhang', 'D.Kim', 'E.Lee', 'F.Singh', 'L.Das', 'V.Kumar', 'G.Novak', 'S.Khalil', 'M.Tucker', 'G.Evans', 'H.Garcia', 'S.Williams', 'I.Murphy', 'J.Wang', 'K.Jayawardene', 'D.Miller', 'K.Patel', 'L.Olsen', 'M.Brown', 'M.Star', 'C.Martinez', 'M.Jensen', 'K.Jones', 'B.Wilson', 'N.Martinez', 'L.Anderson', 'O.Thompson', 'J.Taylor', 'P.Williams', 'A.Johnson', 'Q.Smith', 'H.Davis']
attackerCountry = ['Spain', 'Mexico', 'England', 'China', 'South Korea', 'South Korea', 'India', 'India', 'India', 'Czech Republic', 'Egypt', 'England', 'China', 'Argentina', 'England', 'Ireland', 'China', 'Sri Lanka', 'Canada', 'India', 'Denmark', 'France', 'Poland', 'Mexico', 'Denmark', 'Japan', 'Australia', 'Argentina', 'India', 'Australia', 'Germany', 'Australia', 'U.S.A.', 'England', 'Brazil']
attackerRating = ['93', '92', '91', '89', '87', '85', '83', '82', '81', '81', '80', '79', '79', '79', '78', '78', '76', '75', '75', '74', '73','69', '69', '68', '68', '67','67', '66', '66', '66', '66', '64', '63', '62', '61'] 

# teams
teamName = ["Warwick Warriors", "Stratford Saints", "Cambridge Cheetahs", "Croydon Cats", "Telford Tigers", "Bristol Bulls", "Coventry Cougars", "Sheffield Spiders", "Bath Bulldogs", "Luton Lions", "Leeds Lions", "Newcastle Nights", "Leicester Lions", "Wolverhampton Wizards", "Liverpool Lions" ,"Birmingham Bears","London Leopards", "Manchester Mandems","Leamington Lions","Oxford Opponents"
]
teamRating = [91, 90, 86, 85, 83, 83, 83, 81, 80, 79, 78, 75, 74, 74, 73, 70, 65, 60, 60, 50]

# function for home page
def homePage(coins):
  clear()
  print("")
  print("HOME")
  print("")
  print("Play     - 1")
  print("Store    - 2")
  print("My Squad - 3")
  print("Settings - 4")
  print("Exit     - 5")
  print("")
  f = open("coins.txt", "r")
  coinString = f.read()
  coins = int(coinString)
  print("Current Coin Balance: " + str(coins))
  print("Your team name: " + yourteamname)
  inputNum = input("Enter the number of what you would like to do: ")
  while inputNum != "1" and  inputNum != "2" and inputNum != "3" and inputNum != "4" and inputNum != "5":
    print("")
    print("Please enter a valid option!")
    time.sleep(1.5)
    clear()
    print("")
    print("HOME")
    print("")
    print("Play     - 1")
    print("Store    - 2")
    print("My Squad - 3")
    print("Settings - 4")
    print("Exit     - 5")
    print("")
    f = open("coins.txt", "r")
    coinString = f.read()
    coins = int(coinString)
    print("Current Coin Balance: " + str(coins))
    print("Your team name: " + yourteamname)
    inputNum = input("Enter the number of what you would like to do: ")
  if inputNum == "2":
    print(storePage(coins))
  elif inputNum == "1":
    print(beforeplaypage())
  elif inputNum == "3":
    print(mysquadPage(coins))
  elif inputNum == "5":
    print(exitPage())
  elif inputNum == "4":
    print(settingsPage())
def settingsPage():
  clear()
  global wins
  global losses
  global draws
  global password
  global yourteamname
  global matches
  print("")
  print("SETTINGS")
  print("")
  print("Change Team Name   - 1")
  print("Change Password    - 2")
  print("View match history - 3")
  print("Return to home     - 4")
  print("")
  inputNum = input("Enter the number of what you would like to do: ")
  if inputNum == "1":
    clear()
    print("")
    changename = input("Enter your new team name: ")
    yourteamname = changename
    f = open("username.txt", "w")
    f.write(yourteamname)
    f.close()
    time.sleep(1)
    print("")
    print("Saving...")
    time.sleep(3)
    print("")
    print("Changes saved!")
    time.sleep(2)
    print(settingsPage())
  elif inputNum == "2":
    clear()
    print("")
    editpassword = input("Enter your current password: ")
    if editpassword != password:
      time.sleep(0.5)
      print("")
      print("Incorrect password!")
      time.sleep(2)
      print(settingsPage())
    else:
      password = input("Enter your new password: ")
      confirmpassword = input("Confirm your password: ")
      while password != confirmpassword:
        print("ERROR: The passwords you typed do not match")
        password = input("Enter your new password: ")
        confirmpassword = input("Confirm your password: ")
      f = open("password.txt", "w")
      f.write(password)
      f.close()
      time.sleep(1)
      print("")
      print("Saving...")
      time.sleep(3)
      print("")
      print("Changes saved!")
      time.sleep(2)
      print(settingsPage())
  elif inputNum == "3":
    clear()
    print("")
    print("Your match history: ")
    print("")
    f = open("matches.txt", "r")
    matches = f.read()
    matches = int(matches)
    f.close()
    print("Total matches played: " + str(matches))
    f = open("wins.txt", "r")
    wins = f.read()
    f.close()
    print("Wins: " + wins)
    f = open("draws.txt", "r")
    draws = f.read()
    f.close()
    print("Draws: " + draws)
    f = open("losses.txt", "r")
    losses = f.read()
    f.close()
    print("Losses: " + losses)
    print("")
    f = open("matchhistory.txt", "r")
    history = f.read()
    print(history)
    print("")
    back = input("Press enter to return to settings: ")
    print(settingsPage())
  elif inputNum == "4":
    print(homePage(coins))

#function for exit page
def exitPage():
  clear()
  print("")
  exit = input("Are you sure you want to exit?(y/n): ")
  while exit != "y" and exit != "n":
    print("")
    print("Please enter a valid option!")
    print("")
    exit = input("Are you sure you want to exit?(y/n): ")
  if exit == "n":
    print(homePage(coins))
  else:
    time.sleep(2)
    print("")
    print("Exiting...")
    time.sleep(1)
    clear()
    sys.exit()

# function for store page
def storePage(coins):
  global choosepack
  clear()
  print("")
  print("STORE")
  print("")
  print("View Defender Packs          - 1")
  print("View Midfielder Packs        - 2")
  print("View Attacker Packs          - 3")
  print("Return to Home               - 4")
  print("")
  print("Current Coin Balance: " + str(coins))
  inputNum = input("Enter the number of what you would like to do: ")
  while inputNum != "1" and inputNum != "2" and inputNum != "3" and inputNum != "4":
    print("")
    print("Please enter a valid option!")
    print("")
    inputNum = input("Enter the number of what you would like to do: ")
  clear()
  if inputNum == "1":
    print("")
    print("Regular defender pack - 300 coins  - 1")
    print("Prime defender pack - 1000 coins   - 2")
    print("Premium defender pack - 1500 coins - 3")
    print("Return to store                    - 4")
    print("")
    print("Current Coin Balance: " + str(coins))
    inputNum2 = input("Enter the number of what you would like to do: ")
    while inputNum2 != "1" and inputNum2 != "2" and inputNum2 != "3" and inputNum2 != "4":
      print("")
      print("Please enter a valid option!")
      print("")
      inputNum2 = input("Enter the number of what you would like to do: ")
    if inputNum2 == "1":
      choosepack = '1'
    elif inputNum2 == "2":
      choosepack = '2'
    elif inputNum2 == "3":
      choosepack = '3'
    elif inputNum2 == "4":
      print(storePage(coins))
    print(defenderPack(coins))
  elif inputNum == "2":
    print("")
    print("Regular midfielder pack - 300 coins  - 1")
    print("Prime midfielder pack - 1000 coins   - 2")
    print("Premium midfielder pack - 1500 coins - 3")
    print("Return to store                      - 4")
    print("")
    print("Current Coin Balance: " + str(coins))
    inputNum2 = input("Enter the number of what you would like to do: ")
    while inputNum2 != "1" and inputNum2 != "2" and inputNum2 != "3" and inputNum2 != "4":
      print("")
      print("Please enter a valid option!")
      print("")
      inputNum2 = input("Enter the number of what you would like to do: ")
    if inputNum2 == "1":
      choosepack = '1'
    elif inputNum2 == "2":
      choosepack = '2'
    elif inputNum2 == "3":
      choosepack = '3'
    elif inputNum2 == "4":
      print(storePage(coins))
    print(midfielderPack(coins))
  elif inputNum == "3":
    print("")
    print("Regular attacker pack - 300 coins  - 1")
    print("Prime attacker pack - 1000 coins   - 2")
    print("Premium attacker pack - 1500 coins - 3")
    print("Return to store                    - 4")
    print("")
    print("Current Coin Balance: " + str(coins))
    inputNum2 = input("Enter the number of what you would like to do: ")
    while inputNum2 != "1" and inputNum2 != "2" and inputNum2 != "3" and inputNum2 != "4":
      print("")
      print("Please enter a valid option!")
      print("")
      inputNum2 = input("Enter the number of what you would like to do: ")
    if inputNum2 == "1":
      choosepack = '1'
    elif inputNum2 == "2":
      choosepack = '2'
    elif inputNum2 == "3":
      choosepack = '3'
    elif inputNum2 == "4":
      print(storePage(coins))
    print(attackerPack(coins))
  elif inputNum == "4":
    print(homePage(coins))



# set up the random pack for defenders, midfielders and attackers
def defenderChance():
  import random
  global choosepack
  if choosepack == '1': 
    defpickNum = random.randint(0,49)
  elif choosepack == '2':
    defpickNum = random.randint(0,29)
  elif choosepack == '3':
    defpickNum = random.randint(0,24)
  return defpickNum

def midfielderChance():
  import random
  global choosepack
  if choosepack == '1': 
    midpickNum = random.randint(0,47)
  elif choosepack == '2':
    midpickNum = random.randint(0,27)
  elif choosepack == '3':
    midpickNum = random.randint(0,20)
  return midpickNum

def attackerChance():
  import random
  global choosepack
  if choosepack == '1': 
    attpickNum = random.randint(0,34)
  elif choosepack == '2':
    attpickNum = random.randint(0,20)
  elif choosepack == '3':
    attpickNum = random.randint(0,18)
  return attpickNum

# set up the packing methods for all positions
def defenderPack(coins):
  decision = input("Are you sure you would like to purchase this defender pack? (y/n): ")
  while decision != "y" and decision != "n":
    print("")
    print("Please enter a valid option!")
    print("")
    decision = input("Are you sure you would like to purchase this defender pack? (y/n): ")
  import time
  if coins < 300:
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(1)
    print("")
    print("ERROR: You do not have enough coins to purchase this item!")
    print("")
    time.sleep(3)
    decision = "n"
  if decision == "y":
    defenderNum = defenderChance()
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(3)
    print("")
    print("Country - " + defenderCountry[defenderNum])
    time.sleep(1)
    print("Position - DEF")
    time.sleep(1)
    print(defenderRating[defenderNum] + " OVR")
    time.sleep(1)
    print("Name - " + defenderName[defenderNum])
    print("")
    time.sleep(2)
    f = open("defendername.txt", "r")
    quicksellflag = False
    linecount = 0
    for line in f:
      linecount = linecount+1
      line = line.strip()
      if defenderName[defenderNum] == line:
        print("")
        print("ERROR: You already have this player in your squad!")
        print("")
        quicksellduplicate = quicksell(attackerRating[attackerNum])
        quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        while quicksellstore != "y" and quicksellstore != "n":
          print("")
          print("Please enter a valid option!")
          print("")
          quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        while quicksellstore == "n":
          print('\n' + "ERROR: You must quick sell this player!" + '\n')
          quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
          while quicksellstore != "y" and quicksellstore != "n":
            print("")
            print("Please enter a valid option!")
            print("")
            quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        time.sleep(2)
        print('\n' + "Player quick sold!" + '\n')
        coins = coins - 300
        coins = coins + quicksellduplicate
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        print("Current coin balance: " + str(coins))
        quicksellflag = True
        break
    f.close()
    if quicksellflag == False:
      print("Saving player...")
      time.sleep(3)
      f = open("defendername.txt", "a")
      f.write(defenderName[defenderNum] + '\n')
      f.close()
      f = open("defenderrating.txt", "a")
      f.write(defenderRating[defenderNum] + '\n')
      f.close()
      f = open("defendercountry.txt", "a")
      f.write(defenderCountry[defenderNum] + '\n')
      f.close()
      print("")
      print("Player saved to my squad")
      if choosepack == '1': 
        coins = coins - 300
      elif choosepack == '2':
        coins = coins - 1000
      elif choosepack == '3':
        coins = coins - 1500
      coinString = str(coins)
      f = open("coins.txt", "w")
      f.write(coinString)
      f.close()
    time.sleep(1)
    print("Current coin balance: " + str(coins))
    time.sleep(1)
    decision2 = input("Do you want to open another defender pack? (y/n): ")
    while decision2 != "y" and decision2 != "n":
        print("Please enter a valid option!")
        print("")
        decision2 = input("Do you want to open another defender pack? (y/n): ")
    if decision2 == "y":
      defenderPack(coins)
    elif decision2 == "n":
      print(storePage(coins))
  elif decision == "n":
    print(storePage(coins))

def midfielderPack(coins):
  decision = input("Are you sure you would like to purchase this midfielder pack? (y/n): ")
  while decision != "y" and decision != "n":
    print("")
    print("Please enter a valid option!")
    print("")
    decision = input("Are you sure you would like to purchase this midfielder pack? (y/n): ")
  import time
  if coins < 300:
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(1)
    print("")
    print("ERROR: You do not have enough coins to purchase this item!")
    print("")
    time.sleep(3)
    decision = "n"
  if decision == "y":
    midfielderNum = midfielderChance()
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(3)
    print("")
    print("Country - " + midfielderCountry[midfielderNum])
    time.sleep(1)
    print("Position - MID")
    time.sleep(1)
    print(midfielderRating[midfielderNum] + " OVR")
    time.sleep(1)
    print("Name - " + midfielderName[midfielderNum])
    print("")
    time.sleep(2)
    f = open("midfieldername.txt", "r")
    quicksellflag = False
    linecount = 0
    for line in f:
      linecount = linecount+1
      line = line.strip()
      if midfielderName[midfielderNum] == line:
        print("")
        print("ERROR: You already have this player in your squad!")
        print("")
        quicksellduplicate = quicksell(attackerRating[attackerNum])
        quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        while quicksellstore != "y" and quicksellstore != "n":
          print("")
          print("Please enter a valid option!")
          print("")
          quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        while quicksellstore == "n":
          print('\n' + "ERROR: You must quick sell this player!" + '\n')
          quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
          while quicksellstore != "y" and quicksellstore != "n":
            print("")
            print("Please enter a valid option!")
            print("")
            quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        time.sleep(2)
        print('\n' + "Player quick sold!" + '\n')
        coins = coins - 300
        coins = coins + quicksellduplicate
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        print("Current coin balance: " + str(coins))
        quicksellflag = True
        break
    f.close()
    if quicksellflag == False:
      print("Saving player...")
      time.sleep(3)
      f = open("midfieldername.txt", "a")
      f.write(midfielderName[midfielderNum] + '\n')
      f.close()
      f = open("midfielderrating.txt", "a")
      f.write(midfielderRating[midfielderNum] + '\n')
      f.close()
      f = open("midfieldercountry.txt", "a")
      f.write(midfielderCountry[midfielderNum] + '\n')
      f.close()
      print("")
      print("Player saved to My Squad")
      if choosepack == '1': 
        coins = coins - 300
      elif choosepack == '2':
        coins = coins - 1000
      elif choosepack == '3':
        coins = coins - 1500
      coinString = str(coins)
      f = open("coins.txt", "w")
      f.write(coinString)
      f.close()
    time.sleep(1)
    print("Current coin balance: " + str(coins))
    time.sleep(1)
    decision2 = input("Do you want to open another midfielder pack? (y/n): ")
    while decision2 != "y" and decision2 != "n":
        print("")
        print("Please enter a valid option!")
        print("")
        decision2 = input("Do you want to open another midfielder pack? (y/n): ")
        print("")
    if decision2 == "y":
      print(midfielderPack(coins))
    elif decision2 == "n":
      print(storePage(coins))
  else:
    print(storePage(coins))

def attackerPack(coins):
  decision = input("Are you sure you would like to purchase this attacker pack? (y/n): ")
  while decision != "y" and decision != "n":
    print("")
    print("Please enter a valid option!")
    print("")
    decision = input("Are you sure you would like to purchase this attacker pack? (y/n): ")
  import time
  if coins < 300 and choosepack == '1':
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(1)
    print("")
    print("ERROR: You do not have enough coins to purchase this item!")
    print("")
    time.sleep(3)
    decision = "n"
  elif coins < 1000 and choosepack == '2':
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(1)
    print("")
    print("ERROR: You do not have enough coins to purchase this item!")
    print("")
    time.sleep(3)
    decision = "n"
  elif coins < 1500 and choosepack == '3':
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(1)
    print("")
    print("ERROR: You do not have enough coins to purchase this item!")
    print("")
    time.sleep(3)
    decision = "n"
  if decision == "y":
    attackerNum = attackerChance()
    time.sleep(1)
    print("")
    print("Loading...")
    time.sleep(3)
    print("")
    print("")
    print("Country - " + attackerCountry[attackerNum])
    time.sleep(1)
    print("Position - ATT")
    time.sleep(1)
    print(attackerRating[attackerNum] + " OVR")
    time.sleep(1)
    print("Name - " + attackerName[attackerNum])
    print("")
    time.sleep(2)
    f = open("attackername.txt", "r")
    quicksellflag = False
    linecount = 0
    for line in f:
      linecount = linecount+1
      line = line.strip()
      if attackerName[attackerNum] == line:
        print("")
        print("ERROR: You already have this player in your squad!")
        print("")
        quicksellduplicate = quicksell(attackerRating[attackerNum])
        quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        while quicksellstore != "y" and quicksellstore != "n":
          print("")
          print("Please enter a valid option!")
          print("")
          quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        while quicksellstore == "n":
          print('\n' + "ERROR: You must quick sell this player!" + '\n')
          quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
          while quicksellstore != "y" and quicksellstore != "n":
            print("")
            print("Please enter a valid option!")
            print("")
            quicksellstore = input("Quick sell player for " + str(quicksellduplicate) + " coins?(y/n): ")
        time.sleep(2)
        print('\n' + "Player quick sold!" + '\n')
        coins = coins - 300
        coins = coins + quicksellduplicate
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        print("Current coin balance: " + str(coins))
        quicksellflag = True
        break
    f.close()
    if quicksellflag == False:
      print("Saving player...")
      time.sleep(3)
      f = open("attackername.txt", "a")
      f.write(attackerName[attackerNum] + '\n')
      f.close()
      f = open("attackerrating.txt", "a")
      f.write(attackerRating[attackerNum] + '\n')
      f.close()
      f = open("attackercountry.txt", "a")
      f.write(attackerCountry[attackerNum] + '\n')
      f.close()
      print("")
      print("Player saved to My Squad")
      if choosepack == '1': 
        coins = coins - 300
      elif choosepack == '2':
        coins = coins - 1000
      elif choosepack == '3':
        coins = coins - 1500
      coinString = str(coins)
      f = open("coins.txt", "w")
      f.write(coinString)
      f.close()
    time.sleep(1)
    print("Current coin balance: " + str(coins))
    time.sleep(1)
    print("")
    decision2 = input("Do you want to open another attacker pack? (y/n): ")
    while decision2 != "y" and decision2 != "n":
        print("")
        print("Please enter a valid option!")
        print("")
        decision2 = input("Do you want to open another attacker pack? (y/n): ")
        print("")
    if decision2 == "y":
      print(attackerPack(coins))
    elif decision2 == "n":
      print(storePage(coins))
  else:
    print(storePage(coins))

def beforeplaypage():
  global game
  global points
  global league
  clear()
  print("")
  print("PLAY")
  print("")
  if league == 4:
    print("League " + str(league))
    print("")
    print("Promotion:      14 points")
    print("Title:          23 points")
    print("Current points: " + str(points) + " points")
  elif league == 1:
    print("League " + str(league))
    print("")
    print("Relegation:     14 points")
    print("Title:          23 points")
    print("Current points: " + str(points) + " points")
  else:
    print("League " + str(league))
    print("")
    print("Relegation:     7 points")
    print("Promotion:      14 points")
    print("Title:          23 points")
    print("Current points: " + str(points) + " points")
  print("Games remaining: " + str(game) + " games")
  print("")
  print("Go to match                  - 1")
  print("View all teams in the league - 2")
  print("Return to home               - 3")
  print("")
  playmatch = input("Enter the number of what you would like to do: ")
  while playmatch != "1" and playmatch != "2" and playmatch != "3":
    print("")
    print("Please enter a valid option!")
    print("")
    playmatch = input("Enter the number of what you would like to do: ")
  if playmatch == '1':
    print(playPage(coins))
  elif playmatch == '2':
    print("")
    print("All teams in league " + str(league) + ": ")
    if league == 1:
      for x in range(0, 5):
          print(teamName[x] + " - " + str(teamRating[x]))
    elif league == 2:
      for x in range(5, 10):
          print(teamName[x] + " - " + str(teamRating[x]))
    elif league == 3: 
      for x in range(10, 15):
          print(teamName[x] + " - " + str(teamRating[x]))
    elif league == 4:
      for x in range(15, 20):
          print(teamName[x] + " - " + str(teamRating[x]))
    print("")
    goback = input("Press enter to go back: ")
    print(beforeplaypage())
  elif playmatch == '3':
    print(homePage(coins))

# play page function
def playPage(coins):
  global wins
  global draws
  global losses
  global game
  global points
  global league
  global matches
  clear()
  print("")
  print("PLAY")
  print("")
  print("Randomly generating an opponent...")
  time.sleep(5)
  goalString = 0
  oppString = 0
  goal = 0
  goal2 = 0
  if league == 1:
    teamNum = random.randint(0,4)
  elif league == 2:
    teamNum = random.randint(5,9)
  elif league == 3:
    teamNum = random.randint(10,14)
  elif league == 4:
    teamNum = random.randint(15,19)
  f = open("lastteam.txt", "r")
  lastteam = f.read()
  f.close()
  if lastteam == "False":
    opponent = teamName[teamNum]
    f = open("lastteamnum.txt", "w")
    f.write(str(teamNum))
    f.close()
    f = open("lastteam.txt", "w")
    f.write(opponent)
    f.close()
    lastteam = opponent
  else: 
    opponent = lastteam
    f = open("lastteamnum.txt", "r")
    teamNum = f.read()
    teamNum = int(teamNum)
  print("")
  print("You are playing against the " + opponent + "!")
  time.sleep(1)
  f = open("yourteamrating.txt", "r")
  yourteamratingstring = f.read()
  yourteamrating = int(yourteamratingstring)
  print("Your team Rating: " + str(yourteamrating) + " OVR")
  time.sleep(0.5)
  print("Opposition Team Rating: " + str(teamRating[teamNum]) + " OVR")
  time.sleep(2)
  print("")
  userInput = input("Do you want to start the game? (y/n): ")
  while userInput != "y" and userInput != "n":
    print("")
    print("Please enter a valid option!")
    print("")
    userInput = input("Do you want to start the game? (y/n): ")
  if userInput == "y":
    yourGoal = 0
    oppGoal = 0
    print("")
    print("The match is beginning in a few seconds...")
    time.sleep(3)
    print("")
    matchstart = input("Press enter to start the game")
    print("")
    print("The match has started!")
    f = open("chem.txt", "r")
    chemistry = f.read()
    chemistry = int(chemistry)
    f.close()
    totalrating = int(yourteamrating) * (0.8+(chemistry/100*0.75))
    totalrating = round(totalrating)
    time.sleep(2)
    for x in range(91):
      if totalrating > 100:
        randomNum = random.randint(1,6)
      elif totalrating == 99:
        randomNum1 = random.randint(1,7)
      elif totalrating == 98:
        randomNum1 = random.randint(1,8)
      elif totalrating == 97:
        randomNum1 = random.randint(1,9)
      elif totalrating == 96:
        randomNum1 = random.randint(1,10)
      elif totalrating == 95:
        randomNum1 = random.randint(1,11)
      elif totalrating == 94:
        randomNum1 = random.randint(1,12)
      elif totalrating > 89 and totalrating < 95:
        randomNum1 = random.randint(1,13)
      elif totalrating > 84 and totalrating < 90:
        randomNum1 = random.randint(1,14)
      elif totalrating > 79 and totalrating < 85:
        randomNum1 = random.randint(1,15)
      elif totalrating > 74 and totalrating < 80:
        randomNum1 = random.randint(1,16)
      elif totalrating > 69 and totalrating < 75:
        randomNum1 = random.randint(1,17)
      elif totalrating > 64 and totalrating < 70:
        randomNum1 = random.randint(1,18)
      elif totalrating > 59 and totalrating < 65:
        randomNum1 = random.randint(1,19)
      elif totalrating > 54 and totalrating < 60:
        randomNum1 = random.randint(1,20)
      elif totalrating < 55 and totalrating > 49:
        randomNum1 = random.randint(1,21)  
      else:
        randomNum1 = random.randint(1,70)
      if teamRating[teamNum] > 94:
        randomNum2 = random.randint(1,10)
      elif teamRating[teamNum] > 89 and teamRating[teamNum] < 95:
        randomNum2 = random.randint(1,12)
      elif teamRating[teamNum] > 84 and teamRating[teamNum] < 90:
        randomNum2 = random.randint(1,15)
      elif teamRating[teamNum] > 79 and teamRating[teamNum] < 85:
        randomNum2 = random.randint(1,17)
      elif teamRating[teamNum] > 74 and teamRating[teamNum] < 80:
        randomNum2 = random.randint(1,20)
      elif teamRating[teamNum] > 69 and teamRating[teamNum] < 75:
        randomNum2 = random.randint(1,22)
      elif teamRating[teamNum] > 64 and teamRating[teamNum] < 70:
        randomNum2 = random.randint(1,25)
      elif teamRating[teamNum] > 59 and teamRating[teamNum] < 65:
        randomNum2 = random.randint(1,27)
      elif teamRating[teamNum] > 54 and teamRating[teamNum] < 60:
        randomNum2 = random.randint(1,30)
      elif teamRating[teamNum] < 55:
        randomNum2 = random.randint(1,32)
      if randomNum1 == 1:
        choosemidfielder = random.randint(1,2)
        midfielderchance = random.randint(1,100)
        chooseattacker = random.randint(1,2)
        attackerchance = random.randint(1,100)
        choosemidfielder = int(choosemidfielder)
        midfielderchance = int(midfielderchance)
        chooseattacker = int(chooseattacker)
        attackerchance = int(attackerchance)
        if choosemidfielder == 1:
          if midfielderchance <= int(ovr3):
            if chooseattacker == 1:
              if attackerchance <= int(ovr5):
                timeX = str(x)
                print(timeX + "  " + startingAttacker1 + " goes for goal..")
                time.sleep(2)
                print("    GOAL!")
                time.sleep(1)
                print("    " + startingAttacker1 + " scores for " + yourteamname + "!")
                yourGoal = yourGoal + 1
                goalString = str(yourGoal)
                oppString = str(oppGoal)
                time.sleep(1)
                print("    - Score: " + yourteamname + " " + goalString + " - " + oppString + " " + opponent)
                goal = goal + 1
                time.sleep(2)
              else:
                timeX = str(x)
                print(timeX + "  " + startingAttacker1 + " goes for goal..")
                time.sleep(2)
                print("    Wide!")
                time.sleep(2)
            else:
              if attackerchance <= int(ovr6):
                timeX = str(x)
                print(timeX + "  " + startingAttacker2 + " goes for goal..")
                time.sleep(2)
                print("    GOAL!")
                time.sleep(1)
                print("    " + startingAttacker2 + " scores for " + yourteamname + "!")
                yourGoal = yourGoal + 1
                goalString = str(yourGoal)
                oppString = str(oppGoal)
                time.sleep(1)
                print("   - Score: " + yourteamname + " " + goalString + " - " + oppString + " " + opponent)
                goal = goal + 1
                time.sleep(2)
              else:
                timeX = str(x)
                print(timeX + "  " + startingAttacker2 + " goes for goal..")
                time.sleep(2)
                print("    Wide!")
                time.sleep(2)
        else: 
          if midfielderchance <= int(ovr4):
            if chooseattacker == 1:
              if attackerchance <= int(ovr5):
                timeX = str(x)
                print(timeX + "  " + startingAttacker1 + " goes for goal..")
                time.sleep(2)
                print("    GOAL!")
                time.sleep(1)
                print("    " + startingAttacker1 + " scores for " + yourteamname + "!")
                yourGoal = yourGoal + 1
                goalString = str(yourGoal)
                oppString = str(oppGoal)
                time.sleep(1)
                print("    - Score: " + yourteamname + " " + goalString + " - " + oppString + " " + opponent)
                goal = goal + 1
                time.sleep(2)
              else:
                timeX = str(x)
                print(timeX + "  " + startingAttacker1 + " goes for goal..")
                time.sleep(2)
                print("    Wide!")
                time.sleep(2)
            else:
              if attackerchance <= int(ovr6):
                timeX = str(x)
                print(timeX + "  " + startingAttacker2 + " goes for goal..")
                time.sleep(2)
                print("    GOAL!")
                time.sleep(1)
                print("    " + startingAttacker2 + " scores for " + yourteamname + "!")
                yourGoal = yourGoal + 1
                goalString = str(yourGoal)
                oppString = str(oppGoal)
                time.sleep(1)
                print("    - Score: " + yourteamname + " " + goalString + " - " + oppString + " " + opponent)
                goal = goal + 1
                time.sleep(2)
              else:
                timeX = str(x)
                print(timeX + "  " + startingAttacker2 + " goes for goal..")
                time.sleep(2)
                print("    Wide!")
                time.sleep(2)
      elif randomNum2 == 1:
        choosedefender = random.randint(1,2)
        defenderchance = random.randint(1,100)
        if choosedefender == 1:
          if defenderchance <= int(ovr1):
            timeX = str(x)
            print(timeX + "  " + opponent + " with a chance on goal...")
            time.sleep(2)
            print("    Brilliant block from " + startingDefender1 + "!")
            time.sleep(2)
          else:
            timeX = str(x)
            oppGoal = oppGoal + 1
            goalString = str(yourGoal)
            oppString = str(oppGoal)
            print(timeX + "  " + opponent + " with a chance on goal...")
            time.sleep(2)
            print("    GOAL!")
            time.sleep(1)
            print("    " + opponent + " score!")
            time.sleep(1)
            print("    - Score: " + yourteamname + " " + goalString + " - " + oppString + " " +  opponent)
            goal2 = goal2 + 1
            time.sleep(2)
        else:
          if defenderchance <= int(ovr2):
            timeX = str(x)
            print(timeX + "  " + opponent + " with a chance on goal...")
            time.sleep(2)
            print("    Brilliant block from " + startingDefender2 + "!")
            time.sleep(2)
          else:
            timeX = str(x)
            oppGoal = oppGoal + 1
            goalString = str(yourGoal)
            oppString = str(oppGoal)
            print(timeX + "  " + opponent + " with a chance on goal...")
            time.sleep(2)
            print("    GOAL!")
            time.sleep(1)
            print("    " + opponent + " score!")
            time.sleep(1)
            print("    - Score: " + yourteamname + " " + goalString + " - " + oppString + " " +  opponent)
            goal2 = goal2 + 1
            time.sleep(2)
      else:
        timeX = str(x)
        print(timeX)
        time.sleep(0.3)
    print("Full time!")
    lastteam = "False" 
    f = open("lastteam.txt", "w")
    f.write("False")
    time.sleep(2)
    print("")
    print("The match has ended! The final score:")
    time.sleep(1)
    print(yourteamname + " " + str(goalString) + " - " + str(oppString) + " " +  opponent)
    f = open("matches.txt", "r")
    matches = f.read()
    matches = int(matches)
    f = open("matchhistory.txt", "a")
    matches = matches + 1
    f = open("matches.txt", "w")
    f.write(str(matches))
    f.close()
    f.write("Game " + str(matches) + " - " + yourteamname + " " + str(goalString) + " - " + str(oppString) + " " +  opponent + "\n")
    f.close()
    print("")
    game = game - 1
    f = open("game.txt", "w")
    f.write(str(game))
    f.close()
    if goalString > oppString:
      wins = wins + 1
      f = open("wins.txt", "w")
      f.write(str(wins))
      f.close()
      points = points + 3
      f = open("points.txt", "w")
      f.write(str(points))
      f.close()
      if yourteamrating < teamRating[teamNum]:
        coins = coins + 200
        time.sleep(0.5)
        print("Match result:        +200")
        print("Goal bonus:          +" + str(goal*10))
        print("Goals conceded:      -" + str(goal2*10))
        print("Total coins earnt:   " + str(200+goal*10-goal2*10))
        coins = coins + (goal*10) - (goal2*10)
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
      elif yourteamrating == teamRating[teamNum]:
        coins = coins + 150
        coinString = str(coins)
        time.sleep(0.5)
        print("Match result:        +150")
        print("Goal bonus:          +" + str(goal*10))
        print("Goals conceded:      -" + str(goal2*10))
        print("Total coins earnt:   " + str(150+goal*10-goal2*10))
        coins = coins + (goal*10) - (goal2*10)
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
      elif yourteamrating > teamRating[teamNum]:
        coins = coins + 100
        time.sleep(0.5)
        print("Match result:        +100")
        print("Goal bonus:          +" + str(goal*10))
        print("Goals conceded:      -" + str(goal2*10))
        print("Total coins earnt:   " + str(100+goal*10-goal2*10))
        coins = coins + (goal*10) - (goal2*10)
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
    elif goalString == oppString:
      draws = draws + 1
      f = open("draws.txt", "w")
      f.write(str(draws))
      f.close()
      points = points + 1
      f = open("points.txt", "w")
      f.write(str(points))
      f.close()
      coins = coins + 50
      time.sleep(0.5)
      print("Match result:        +50")
      print("Goal bonus:          +" + str(goal*10))
      print("Goals conceded:      -" + str(goal2*10))
      print("Total coins earnt:   " + str(50+goal*10-goal2*10))
      coins = coins + (goal*10) - (goal2*10)
      coinString = str(coins)
      f = open("coins.txt", "w")
      f.write(coinString)
      f.close()
    else:
      losses = losses + 1
      f = open("losses.txt", "w")
      f.write(str(losses))
      f.close()
      time.sleep(0.5)
      print("Match result:        +0")
      time.sleep(0.5)
      print("Goal bonus:          +" + str(goal*10))
      time.sleep(0.5)
      print("Goals conceded:      -" + str(goal2*10))
      time.sleep(0.5)
      print("Total coins earnt:   " + str(goal*10-goal2*10))
      coins = coins + (goal*10) - (goal2*10)
    if game == 0:
      if points < 7 and league == 4:
        time.sleep(2)
        print("")
        print("You have stayed in league " + str(league))
        coins = coins + 500
        points = 0
        game = 0
        time.sleep(0.5)
        print("Extra coins earnt: +500")
      elif points < 23 and league == 1:
        time.sleep(2)
        print("")
        print("You have stayed in league " + str(league))
        coins = coins + 500
        points = 0
        game = 0
        time.sleep(0.5)
        print("Extra coins earnt: +500")
      elif points < 6:
        if league != 4:
          league = league + 1
          f = open("league.txt", "w")
          f.write(str(league))
          f.close()
          time.sleep(2)
          print("")
          print("You have been relegated to league " + str(league))
          points = 0
          game = 0
      elif points > 6 and points < 14:
        if league != 1 or league != 4:
          time.sleep(2)
          print("")
          print("You have stayed in league " + str(league))
          coins = coins + 500
          points = 0
          game = 0
          time.sleep(0.5)
          print("Extra coins earnt: +500")
      elif points > 13 and points < 23:
        if league != 1:
          league = league - 1
          f = open("league.txt", "w")
          f.write(str(league))
          f.close()
          coins = coins + 1000
          time.sleep(2)
          print("")
          print("You have been promoted to league " + str(league))
          points = 0
          game = 0
          time.sleep(0.5)
          print("Extra coins earnt: +1000")
      elif points > 22:
        league = league - 1
        f = open("league.txt", "w")
        f.write(str(league))
        f.close()
        time.sleep(2)
        print("")
        print("You have won the title!")
        points = 0
        game = 0
        time.sleep(1)
        if league != 1:
          league = league - 1
          f = open("league.txt", "w")
          f.write(str(league))
          f.close()
          time.sleep(1)
          print("")
          print("You have been promoted to league " + str(league))
        if league == 1:
          time.sleep(0.5)
          print("Extra coins earnt: +3000")
          coins = coins + 3000
        elif league == 2:
          time.sleep(0.5)
          print("Extra coins earnt: +2500")
          coins = coins + 2500
        elif league == 3:
          time.sleep(0.5)
          coins = coins + 2000
          print("Extra coins earnt: +2000")
        elif league == 4:
          time.sleep(0.5)
          coins = coins + 1500
          print("Extra coins earnt: +1500")
    coinString = str(coins)
    f = open("coins.txt", "w")
    f.write(coinString)
    f.close()
    time.sleep(0.5)
    print("Current coin balance: " + str(coins))
    time.sleep(0.5)
    print("")
    playmatch = input("Press enter to continue: ")
    print(beforeplaypage())
  elif userInput == "n":
    print(beforeplaypage())

def sd1(mysquadinput3):
  global startingDefender1
  global ovr1
  global startingcountry1
  mysquadinput3 = int(mysquadinput3)
  f = open("defendername.txt", "r")
  lines = f.readlines()
  lines.append(startingDefender1 + '\n')
  f.close()
  e = open("defenderrating.txt", "r")
  lines2 = e.readlines()
  lines2.append(ovr1 + '\n')
  e.close()
  f = open("defendercountry.txt", "r")
  lines3 = f.readlines()
  lines3.append(startingcountry1 + '\n')
  f.close()
  f = open("defendername.txt", "w")
  f.writelines(lines)
  f.close()
  e = open("defenderrating.txt", "w")
  e.writelines(lines2)
  e.close()
  e = open("defendercountry.txt", "w")
  e.writelines(lines3)
  e.close()
  f = open("defendername.txt", "r")
  e = open("defenderrating.txt", "r")
  g = open("defendercountry.txt", "r")
  linecount = 0
  for line in f:
    linecount = linecount+1
    line = line.strip()
    if linecount == mysquadinput3:
      startingDefender1 = line
  linecount2 = 0
  for line in e:
    linecount2 = linecount2+1
    line = line.strip()
    if linecount2 == mysquadinput3:
      ovr1 = line
  linecount3 = 0
  for line in g:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingcountry1 = line
  del lines[mysquadinput3 - 1]
  del lines2[mysquadinput3 - 1]
  del lines3[mysquadinput3 - 1]
  f.close()
  e.close()
  g.close()
  f = open("defendername.txt", "w")
  e = open("defenderrating.txt", "w")
  g = open("defendercountry.txt", "w")
  f.writelines(lines)
  e.writelines(lines2)
  g.writelines(lines3)
  f.close()
  e.close()
  g.close()
  time.sleep(2)
  print("Change saved!")
  time.sleep(1)
  f = open("startingdefender1.txt", "w")
  f.write(startingDefender1)
  f.close()
  f = open("ovr1.txt", "w")
  f.write(ovr1)
  f.close()
  f = open("startingcountry1.txt", "w")
  f.write(startingcountry1)
  f.close()

def sd2(mysquadinput3):
  global startingDefender2
  global ovr2
  global startingcountry2
  mysquadinput3 = int(mysquadinput3)
  f = open("defendername.txt", "r")
  lines = f.readlines()
  lines.append(startingDefender2 + '\n')
  f.close()
  e = open("defenderrating.txt", "r")
  lines2 = e.readlines()
  lines2.append(ovr2 + '\n')
  e.close()
  f = open("defendercountry.txt", "r")
  lines3 = f.readlines()
  lines3.append(startingcountry2 + '\n')
  f.close()
  f = open("defendername.txt", "w")
  f.writelines(lines)
  f.close()
  e = open("defenderrating.txt", "w")
  e.writelines(lines2)
  e.close()
  e = open("defendercountry.txt", "w")
  e.writelines(lines3)
  e.close()
  f = open("defendername.txt", "r")
  e = open("defenderrating.txt", "r")
  g = open("defendercountry.txt", "r")
  linecount = 0
  for line in f:
    linecount = linecount+1
    line = line.strip()
    if linecount == mysquadinput3:
      startingDefender2 = line
  linecount2 = 0
  for line in e:
    linecount2 = linecount2+1
    line = line.strip()
    if linecount2 == mysquadinput3:
      ovr2 = line
  linecount3 = 0
  for line in g:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingcountry2 = line
  del lines[mysquadinput3 - 1]
  del lines2[mysquadinput3 - 1]
  del lines3[mysquadinput3 - 1]
  f.close()
  e.close()
  g.close()
  f = open("defendername.txt", "w")
  e = open("defenderrating.txt", "w")
  g = open("defendercountry.txt", "w")
  f.writelines(lines)
  e.writelines(lines2)
  g.writelines(lines3)
  f.close()
  e.close()
  g.close()
  time.sleep(2)
  print("Change saved!")
  time.sleep(1)
  f = open("startingdefender2.txt", "w")
  f.write(startingDefender2)
  f.close()
  f = open("ovr2.txt", "w")
  f.write(ovr2)
  f.close()
  f = open("startingcountry2.txt", "w")
  f.write(startingcountry2)
  f.close()

def sm1(mysquadinput3):
  global startingMidfielder1
  global ovr3
  global startingcountry3
  mysquadinput3 = int(mysquadinput3)
  f = open("midfieldername.txt", "r")
  lines = f.readlines()
  lines.append(startingMidfielder1 + '\n')
  f.close()
  e = open("midfielderrating.txt", "r")
  lines2 = e.readlines()
  lines2.append(ovr3 + '\n')
  e.close()
  f = open("midfieldercountry.txt", "r")
  lines3 = f.readlines()
  lines3.append(startingcountry3 + '\n')
  f.close()
  f = open("midfieldername.txt", "w")
  f.writelines(lines)
  f.close()
  e = open("midfielderrating.txt", "w")
  e.writelines(lines2)
  e.close()
  e = open("midfieldercountry.txt", "w")
  e.writelines(lines3)
  e.close()
  f = open("midfieldername.txt", "r")
  e = open("midfielderrating.txt", "r")
  g = open("midfieldercountry.txt", "r")
  linecount = 0
  for line in f:
    linecount = linecount+1
    line = line.strip()
    if linecount == mysquadinput3:
      startingMidfielder1 = line
  linecount2 = 0
  for line in e:
    linecount2 = linecount2+1
    line = line.strip()
    if linecount2 == mysquadinput3:
      ovr3 = line
  linecount3 = 0
  for line in g:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingcountry3 = line
  del lines[mysquadinput3 - 1]
  del lines2[mysquadinput3 - 1]
  del lines3[mysquadinput3 - 1]
  f.close()
  e.close()
  g.close()
  f = open("midfieldername.txt", "w")
  e = open("midfielderrating.txt", "w")
  g = open("midfieldercountry.txt", "w")
  f.writelines(lines)
  e.writelines(lines2)
  g.writelines(lines3)
  f.close()
  e.close()
  g.close()
  time.sleep(2)
  print("Change saved!")
  time.sleep(1)
  f = open("startingmidfielder1.txt", "w")
  f.write(startingMidfielder1)
  f.close()
  f = open("ovr3.txt", "w")
  f.write(ovr3)
  f.close()
  f = open("startingcountry3.txt", "w")
  f.write(startingcountry3)
  f.close()

def sm2(mysquadinput3):
  global startingMidfielder2
  global ovr4
  global startingcountry4
  mysquadinput3 = int(mysquadinput3)
  f = open("midfieldername.txt", "r")
  lines = f.readlines()
  lines.append(startingMidfielder2 + '\n')
  f.close()
  e = open("midfielderrating.txt", "r")
  lines2 = e.readlines()
  lines2.append(ovr4 + '\n')
  e.close()
  f = open("midfieldercountry.txt", "r")
  lines3 = f.readlines()
  lines3.append(startingcountry4 + '\n')
  f.close()
  f = open("midfieldername.txt", "w")
  f.writelines(lines)
  f.close()
  e = open("midfielderrating.txt", "w")
  e.writelines(lines2)
  e.close()
  e = open("midfieldercountry.txt", "w")
  e.writelines(lines3)
  e.close()
  f = open("midfieldername.txt", "r")
  e = open("midfielderrating.txt", "r")
  g = open("midfieldercountry.txt", "r")
  linecount = 0
  for line in f:
    linecount = linecount+1
    line = line.strip()
    if linecount == mysquadinput3:
      startingMidfielder2 = line
  linecount2 = 0
  for line in e:
    linecount2 = linecount2+1
    line = line.strip()
    if linecount2 == mysquadinput3:
      ovr4 = line
  linecount3 = 0
  for line in g:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingcountry4 = line
  del lines[mysquadinput3 - 1]
  del lines2[mysquadinput3 - 1]
  del lines3[mysquadinput3 - 1]
  f.close()
  e.close()
  g.close()
  f = open("midfieldername.txt", "w")
  e = open("midfielderrating.txt", "w")
  g = open("midfieldercountry.txt", "w")
  f.writelines(lines)
  e.writelines(lines2)
  g.writelines(lines3)
  f.close()
  e.close()
  g.close()
  time.sleep(2)
  print("Change saved!")
  time.sleep(1)
  f = open("startingmidfielder2.txt", "w")
  f.write(startingMidfielder2)
  f.close()
  f = open("ovr4.txt", "w")
  f.write(ovr4)
  f.close()
  f = open("startingcountry4.txt", "w")
  f.write(startingcountry4)
  f.close()

def sa1(mysquadinput3):
  global startingAttacker1
  global ovr5
  global startingcountry5
  mysquadinput3 = int(mysquadinput3)
  f = open("attackername.txt", "r")
  lines = f.readlines()
  lines.append(startingAttacker1 + '\n')
  f.close()
  e = open("attackerrating.txt", "r")
  lines2 = e.readlines()
  lines2.append(ovr5 + '\n')
  e.close()
  f = open("attackercountry.txt", "r")
  lines3 = f.readlines()
  lines3.append(startingcountry5 + '\n')
  f.close()
  f = open("attackername.txt", "w")
  f.writelines(lines)
  f.close()
  e = open("attackerrating.txt", "w")
  e.writelines(lines2)
  e.close()
  e = open("attackercountry.txt", "w")
  e.writelines(lines3)
  e.close()
  f = open("attackername.txt", "r")
  e = open("attackerrating.txt", "r")
  g = open("attackercountry.txt", "r")
  linecount = 0
  for line in f:
    linecount = linecount+1
    line = line.strip()
    if linecount == mysquadinput3:
      startingAttacker1 = line
  linecount2 = 0
  for line in e:
    linecount2 = linecount2+1
    line = line.strip()
    if linecount2 == mysquadinput3:
      ovr5 = line
  linecount3 = 0
  for line in g:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingcountry5 = line
  del lines[mysquadinput3 - 1]
  del lines2[mysquadinput3 - 1]
  del lines3[mysquadinput3 - 1]
  f.close()
  e.close()
  g.close()
  f = open("attackername.txt", "w")
  e = open("attackerrating.txt", "w")
  g = open("attackercountry.txt", "w")
  f.writelines(lines)
  e.writelines(lines2)
  g.writelines(lines3)
  f.close()
  e.close()
  g.close()
  time.sleep(2)
  print("Change saved!")
  time.sleep(1)
  f = open("startingattacker1.txt", "w")
  f.write(startingAttacker1)
  f.close()
  f = open("ovr5.txt", "w")
  f.write(ovr5)
  f.close()
  f = open("startingcountry5.txt", "w")
  f.write(startingcountry5)
  f.close()

def sa2(mysquadinput3):
  global startingAttacker2
  global ovr6
  global startingcountry6
  mysquadinput3 = int(mysquadinput3)
  f = open("attackername.txt", "r")
  lines = f.readlines()
  lines.append(startingAttacker2 + '\n')
  f.close()
  e = open("attackerrating.txt", "r")
  lines2 = e.readlines()
  lines2.append(ovr6 + '\n')
  e.close()
  f = open("attackercountry.txt", "r")
  lines3 = f.readlines()
  lines3.append(startingcountry6 + '\n')
  f.close()
  f = open("attackername.txt", "w")
  f.writelines(lines)
  f.close()
  e = open("attackerrating.txt", "w")
  e.writelines(lines2)
  e.close()
  e = open("defendercountry.txt", "w")
  e.writelines(lines3)
  e.close()
  f = open("attackername.txt", "r")
  e = open("attackerrating.txt", "r")
  g = open("attackercountry.txt", "r")
  linecount3 = 0
  for line in f:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingAttacker2 = line
  linecount4 = 0
  for line in e:
    linecount4 = linecount4+1
    line = line.strip()
    if linecount4 == mysquadinput3:
      ovr6 = line
  linecount3 = 0
  for line in g:
    linecount3 = linecount3+1
    line = line.strip()
    if linecount3 == mysquadinput3:
      startingcountry6 = line
  del lines[mysquadinput3 - 1]
  del lines2[mysquadinput3 - 1]
  del lines3[mysquadinput3 - 1]
  f.close()
  e.close()
  g.close()
  f = open("attackername.txt", "w")
  e = open("attackerrating.txt", "w")
  g = open("attackercountry.txt", "w")
  f.writelines(lines)
  e.writelines(lines2)
  g.writelines(lines3)
  f.close()
  e.close()
  g.close()
  time.sleep(2)
  print("Change saved!")
  time.sleep(1)
  f = open("startingattacker2.txt", "w")
  f.write(startingAttacker2)
  f.close()
  f = open("ovr6.txt", "w")
  f.write(ovr6)
  f.close()
  f = open("startingcountry6.txt", "w")
  f.write(startingcountry6)
  f.close()

def quicksell(rating):
  rating = int(rating)
  if rating < 60:
    rating2 = rating - 50
    rating = 10 + rating2*5
  elif rating < 70 and rating > 59:
    rating2 = rating - 60
    rating = 10 + rating2*10
  elif rating < 80 and rating > 69:
    rating2 = rating - 70
    rating = 120 + rating2*20
  elif rating < 90 and rating > 79:
    rating2 = rating - 80
    rating = 320 + rating2*150
  elif rating < 95 and rating > 89:
    rating2 = rating - 90
    rating = 1000 + rating2*500
  else:
    rating2 = rating - 95
    rating = 10000 + rating2*5000
  return rating

def calculatechemistry():
  global chemistry
  chemistry = 0
  global startingcountry1
  global startingcountry2
  global startingcountry3
  global startingcountry4
  global startingcountry5
  global startingcountry6
  if startingcountry1 == startingcountry2:
    chemistry = chemistry + 10
  if startingcountry3 == startingcountry4:
    chemistry = chemistry + 10
  if startingcountry5 == startingcountry6:
    chemistry = chemistry + 10
  if startingcountry1 == startingcountry3 or startingcountry1 == startingcountry4 or startingcountry1 == startingcountry5 or startingcountry1 == startingcountry6:
    chemistry = chemistry + 5
  if startingcountry2 == startingcountry3 or startingcountry2 == startingcountry4 or startingcountry2 == startingcountry5 or startingcountry2 == startingcountry6:
    chemistry = chemistry + 5
  if startingcountry3 == startingcountry4 or startingcountry3 == startingcountry5 or startingcountry3 == startingcountry6:
    chemistry = chemistry + 5
  if startingcountry4 == startingcountry5 or startingcountry4 == startingcountry6:
    chemistry = chemistry + 5
  if startingcountry5 == startingcountry6:
    chemistry = chemistry + 5
  return chemistry

def viewplayerPage(coins):
  global startingDefender1
  global startingDefender2
  global startingMidfielder1
  global startingMidfielder2
  global startingAttacker1
  global startingAttacker2
  global startingcountry1
  global startingcountry2
  global startingcountry3
  global startingcountry4
  global startingcountry5
  global startingcountry6
  global ovr1
  global ovr2
  global ovr3
  global ovr4
  global ovr5
  global ovr6
  print("")
  clear()
  print("")
  print("1 - DEF - " + startingDefender1 + " - " + startingcountry1 + " - " + ovr1)
  print("2 - DEF - " + startingDefender2 + " - " + startingcountry2 + " - " + ovr2)
  print("3 - MID - " + startingMidfielder1 + " - " + startingcountry3 + " - " + " - " + ovr3)
  print("4 - MID - " + startingMidfielder2 + " - " + startingcountry4 + " - " + " - " + ovr4)
  print("5 - ATT - " + startingAttacker1 + " - " + startingcountry5 + " - " + " - " + ovr5)
  print("6 - ATT - " + startingAttacker2 + " - " + startingcountry6 + " - " + " - " + ovr6)
  print("")
  print("e - Return to My Squad")
  print("")
  mysquadinput2 = input("Enter the number of what player's information you would like to view: ")
  mysquadinput2 = str(mysquadinput2)
  while mysquadinput2 != '1' and mysquadinput2 != '2' and mysquadinput2 != '3' and mysquadinput2 != '4' and mysquadinput2 != '5' and mysquadinput2 != '6' and mysquadinput2 != 'e':
    print("")
    print("Please enter a valid option!")
    print("")
    mysquadinput2 = input("Enter the number of what player's information you would like to view: ")
    mysquadinput2 = str(mysquadinput2)
  if mysquadinput2 == '1':
    clear()
    print("")
    print("Name - " + startingDefender1)
    print("Rating - " + ovr1 + " OVR")
    print("Position - DEF")
    print("Nationality - " + startingcountry1)
    quicksellrating1 = int(ovr1)
    quicksellrating2 = quicksell(quicksellrating1)
    print("Quick sell for " + str(quicksellrating2) + " coins")
    print("")
    print("Quick sell player   - 1")
    print("Return to My Squad - 2")
    print("")
    mysquadinput3 = input("Enter the number of what you would like to do: ")
    mysquadinput3 = str(mysquadinput3)
    while mysquadinput3 != '1' and mysquadinput3 != '2':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput3 = input("Enter the number of what you would like to do: ")
      mysquadinput3 = str(mysquadinput3)
    if mysquadinput3 == '1':
      mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
      mysquadinput4 = str(mysquadinput4)
      while mysquadinput4 != 'y' and mysquadinput4 != 'n':
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
        mysquadinput4 = str(mysquadinput4)
      if mysquadinput4 == 'y':
        e = open("defendername.txt", "r")
        content = e.read()
        e.close()
        print("")
        if len(content) == 0:
          time.sleep(2)
          print("ERROR: You have no replacements")
          time.sleep(2)
          print(mysquadPage(coins))
        e = open("defendercountry.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingcountry1 = lastline
        lines.pop()
        f = open("startingcountry1.txt", "w")
        f.write(startingcountry1)
        f.close()
        e = open("defendercountry.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("defendername.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingDefender1 = lastline
        lines.pop()
        f = open("startingdefender1.txt", "w")
        f.write(startingDefender1)
        f.close()
        e = open("defendername.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("defenderrating.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        ovr1 = lastline
        lines.pop()
        e.close()
        e = open("defenderrating.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("ovr1.txt", "w")
        e.write(ovr1)
        e.close()
        coins = coins + quicksellrating2
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        time.sleep(2)
        print("")
        print("Player quick sold for " + str(quicksellrating2) + " coins")
        time.sleep(1)
        print("Current coin balance: " + str(coins))
        time.sleep(3)
        print(viewplayerPage(coins))
      elif mysquadinput4 == 'n':
        print(viewplayerPage(coins))
    elif mysquadinput3 == '2':
      print(mysquadPage(coins))
  elif mysquadinput2 == '2':
    clear()
    print("")
    print("Name - " + startingDefender2)
    print("Rating - " + ovr2 + " OVR")
    print("Position - DEF")
    print("Nationality - " + startingcountry2)
    quicksellrating1 = int(ovr2)
    quicksellrating2 = quicksell(quicksellrating1)
    print("Quick sell for " + str(quicksellrating2) + " coins")
    print("")
    print("Quick sell player   - 1")
    print("Return to My Squad - 2")
    print("")
    mysquadinput3 = input("Enter the number of what you would like to do: ")
    mysquadinput3 = str(mysquadinput3)
    while mysquadinput3 != '1' and mysquadinput3 != '2':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput3 = input("Enter the number of what you would like to do: ")
      mysquadinput3 = str(mysquadinput3)
    if mysquadinput3 == '1':
      mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
      mysquadinput4 = str(mysquadinput4)
      while mysquadinput4 != 'y' and mysquadinput4 != 'n':
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
        mysquadinput4 = str(mysquadinput4)
      if mysquadinput4 == 'y':
        e = open("defendername.txt", "r")
        content = e.read()
        e.close()
        print("")
        if len(content) == 0:
          time.sleep(2)
          print("ERROR: You have no replacements")
          time.sleep(2)
          print(mysquadPage(coins))
        e = open("defendercountry.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingcountry2 = lastline
        lines.pop()
        f = open("startingcountry2.txt", "w")
        f.write(startingcountry2)
        f.close()
        e = open("defendercountry.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("defendername.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        startingDefender2 = lastline
        lines.pop()
        e.close()
        f = open("startingdefender2.txt", "w")
        f.write(startingDefender2)
        f.close()
        e = open("defendername.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("defenderrating.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        ovr2 = lastline
        lines.pop()
        e.close()
        e = open("defenderrating.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("ovr2.txt", "w")
        e.write(ovr2)
        e.close()
        coins = coins + quicksellrating2
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        time.sleep(2)
        print("")
        print("Player quick sold for " + str(quicksellrating2) + " coins")
        time.sleep(1)
        print("Current coin balance: " + str(coins))
        time.sleep(3)
        print(viewplayerPage(coins))
      elif mysquadinput4 == 'n':
        print(viewplayerPage(coins))
    elif mysquadinput3 == '2':
      print(mysquadPage(coins))
  elif mysquadinput2 == '3':
    clear()
    print("")
    print("Name - " + startingMidfielder1)
    print("Rating - " + ovr3 + " OVR")
    print("Position - MID")
    print("Nationality - " + startingcountry3)
    quicksellrating1 = int(ovr3)
    quicksellrating2 = quicksell(quicksellrating1)
    print("Quick sell for " + str(quicksellrating2) + " coins")
    print("")
    print("Quick sell player   - 1")
    print("Return to My Squad - 2")
    print("")
    mysquadinput3 = input("Enter the number of what you would like to do: ")
    mysquadinput3 = str(mysquadinput3)
    while mysquadinput3 != '1' and mysquadinput3 != '2':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput3 = input("Enter the number of what you would like to do: ")
      mysquadinput3 = str(mysquadinput3)
    if mysquadinput3 == '1':
      mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
      mysquadinput4 = str(mysquadinput4)
      while mysquadinput4 != 'y' and mysquadinput4 != 'n':
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
        mysquadinput4 = str(mysquadinput4)
      if mysquadinput4 == 'y':
        e = open("midfieldername.txt", "r")
        content = e.read()
        e.close()
        print("")
        if len(content) == 0:
          time.sleep(2)
          print("ERROR: You have no replacements")
          time.sleep(2)
          print(mysquadPage(coins))
        e = open("defendercountry.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingcountry3 = lastline
        lines.pop()
        f = open("startingcountry3.txt", "w")
        f.write(startingcountry3)
        f.close()
        e = open("defendercountry.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("midfieldername.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        startingMidfielder1 = lastline
        lines.pop()
        e.close()
        f = open("startingmidfielder1.txt", "w")
        f.write(startingMidfielder1)
        f.close()
        e = open("midfieldername.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("midfielderrating.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        ovr3 = lastline
        lines.pop()
        e.close()
        e = open("midfielderrating.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("ovr3.txt", "w")
        e.write(ovr3)
        e.close()
        coins = coins + quicksellrating2
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        time.sleep(2)
        print("")
        print("Player quick sold for " + str(quicksellrating2) + " coins")
        time.sleep(1)
        print("Current coin balance: " + str(coins))
        time.sleep(3)
        print(viewplayerPage(coins))
      elif mysquadinput4 == 'n':
        print(viewplayerPage(coins))
    elif mysquadinput3 == '2':
      print(mysquadPage(coins))
  elif mysquadinput2 == '4':
    clear()
    print("")
    print("Name - " + startingMidfielder2)
    print("Rating - " + ovr4 + " OVR")
    print("Position - MID")
    print("Nationality - " + startingcountry4)
    quicksellrating1 = int(ovr4)
    quicksellrating2 = quicksell(quicksellrating1)
    print("Quick sell for " + str(quicksellrating2) + " coins")
    print("")
    print("Quick sell player   - 1")
    print("Return to My Squad - 2")
    print("")
    mysquadinput3 = input("Enter the number of what you would like to do: ")
    mysquadinput3 = str(mysquadinput3)
    while mysquadinput3 != '1' and mysquadinput3 != '2':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput3 = input("Enter the number of what you would like to do: ")
      mysquadinput3 = str(mysquadinput3)
    if mysquadinput3 == '1':
      mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
      mysquadinput4 = str(mysquadinput4)
      while mysquadinput4 != 'y' and mysquadinput4 != 'n':
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
        mysquadinput4 = str(mysquadinput4)
      if mysquadinput4 == 'y':
        e = open("midfieldername.txt", "r")
        content = e.read()
        e.close()
        print("")
        if len(content) == 0:
          time.sleep(2)
          print("ERROR: You have no replacements")
          time.sleep(2)
          print(mysquadPage(coins))
        e = open("defendercountry.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingcountry4 = lastline
        lines.pop()
        f = open("startingcountry4.txt", "w")
        f.write(startingcountry4)
        f.close()
        e = open("defendercountry.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("midfieldername.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        startingMidfielder2 = lastline
        lines.pop()
        e.close()
        f = open("startingmidfielder2.txt", "w")
        f.write(startingMidfielder2)
        f.close()
        e = open("midfieldername.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("midfielderrating.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        ovr4 = lastline
        lines.pop()
        e.close()
        e = open("midfielderrating.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("ovr4.txt", "w")
        e.write(ovr4)
        e.close()
        coins = coins + quicksellrating2
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        time.sleep(2)
        print("")
        print("Player quick sold for " + str(quicksellrating2) + " coins")
        time.sleep(1)
        print("Current coin balance: " + str(coins))
        time.sleep(3)
        print(viewplayerPage(coins))
      elif mysquadinput4 == 'n':
        print(viewplayerPage(coins))
    elif mysquadinput3 == '2':
        print(mysquadPage(coins))
  elif mysquadinput2 == '5':
    clear()
    print("")
    print("Name - " + startingAttacker1)
    print("Rating - " + ovr5 + " OVR")
    print("Position - ATT")
    print("Nationality - " + startingcountry5)
    quicksellrating1 = int(ovr5)
    quicksellrating2 = quicksell(quicksellrating1)
    print("Quick sell for " + str(quicksellrating2) + " coins")
    print("")
    print("Quick sell player   - 1")
    print("Return to My Squad - 2")
    print("")
    mysquadinput3 = input("Enter the number of what you would like to do: ")
    mysquadinput3 = str(mysquadinput3)
    while mysquadinput3 != '1' and mysquadinput3 != '2':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput3 = input("Enter the number of what you would like to do: ")
      mysquadinput3 = str(mysquadinput3)
    if mysquadinput3 == '1':
      mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
      mysquadinput4 = str(mysquadinput4)
      while mysquadinput4 != 'y' and mysquadinput4 != 'n':
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
        mysquadinput4 = str(mysquadinput4)
      if mysquadinput4 == 'y':
        e = open("attackername.txt", "r")
        content = e.read()
        e.close()
        print("")
        if len(content) == 0:
          time.sleep(2)
          print("ERROR: You have no replacements")
          time.sleep(2)
          print(mysquadPage(coins))
        e = open("defendercountry.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingcountry5 = lastline
        lines.pop()
        f = open("startingcountry5.txt", "w")
        f.write(startingcountry5)
        f.close()
        e = open("defendercountry.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("attackername.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        startingAttacker1 = lastline
        lines.pop()
        e.close()
        f = open("startingattacker1.txt", "w")
        f.write(startingAttacker1)
        f.close()
        e = open("attackername.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("attackerrating.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        ovr5 = lastline
        lines.pop()
        e.close()
        e = open("attackerrating.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("ovr5.txt", "w")
        e.write(ovr5)
        e.close()
        coins = coins + quicksellrating2
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        time.sleep(2)
        print("")
        print("Player quick sold for " + str(quicksellrating2) + " coins")
        time.sleep(1)
        print("Current coin balance: " + str(coins))
        time.sleep(3)
        print(viewplayerPage(coins))
      elif mysquadinput4 == 'n':
        print(viewplayerPage(coins))
    elif mysquadinput3 == '2':
      print(mysquadPage(coins))
  elif mysquadinput2 == 'e':
    print(mysquadPage(coins))
  elif mysquadinput2 == '6':
    clear()
    print("")
    print("Name - " + startingAttacker2)
    print("Rating - " + ovr6 + " OVR")
    print("Position - ATT")
    print("Nationality - " + startingcountry6)
    quicksellrating1 = int(ovr6)
    quicksellrating2 = quicksell(quicksellrating1)
    print("Quick sell for " + str(quicksellrating2) + " coins")
    print("")
    print("Quick sell player   - 1")
    print("Return to My Squad - 2")
    print("")
    mysquadinput3 = input("Enter the number of what you would like to do: ")
    mysquadinput3 = str(mysquadinput3)
    while mysquadinput3 != '1' and mysquadinput3 != '2':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput3 = input("Enter the number of what you would like to do: ")
      mysquadinput3 = str(mysquadinput3)
    if mysquadinput3 == '1':
      mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
      mysquadinput4 = str(mysquadinput4)
      while mysquadinput4 != 'y' and mysquadinput4 != 'n':
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput4 = input("Are you sure you want to quick sell this player for " + str(quicksellrating2) + " coins? (y/n): ")
        mysquadinput4 = str(mysquadinput4)
      if mysquadinput4 == 'y':
        e = open("attackername.txt", "r")
        content = e.read()
        e.close()
        print("")
        if len(content) == 0:
          time.sleep(2)
          print("ERROR: You have no replacements")
          time.sleep(2)
          print(mysquadPage(coins))
        e = open("defendercountry.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        e.close()
        startingcountry6 = lastline
        lines.pop()
        f = open("startingcountry6.txt", "w")
        f.write(startingcountry6)
        f.close()
        e = open("defendercountry.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("attackername.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        startingAttacker2 = lastline
        lines.pop()
        e.close()
        f = open("startingattacker2.txt", "w")
        f.write(startingAttacker2)
        f.close()
        e = open("attackername.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("attackerrating.txt", "r")
        lines = e.readlines()
        lastline = lines[-1].strip()
        ovr6 = lastline
        lines.pop()
        e.close()
        e = open("attackerrating.txt", "w")
        e.writelines(lines)
        e.close()
        e = open("ovr6.txt", "w")
        e.write(ovr6)
        e.close()
        coins = coins + quicksellrating2
        coinString = str(coins)
        f = open("coins.txt", "w")
        f.write(coinString)
        f.close()
        time.sleep(2)
        print("")
        print("Player quick sold for " + str(quicksellrating2) + " coins")
        time.sleep(1)
        print("Current coin balance: " + str(coins))
        time.sleep(3)
        print(viewplayerPage(coins))
      elif mysquadinput4 == 'n':
        print(viewplayerPage(coins))
    elif mysquadinput3 == '2':
      print(mysquadPage(coins)) 

def allplayers():
  clear()
  print("")
  print("View all owned defenders   - 1")
  print("View all owned midfielders - 2")
  print("View all owned attackers   - 3")
  print("Return to My Squad         - 4")
  print("")
  mysquadinput2 = input("Enter the number of what you would like to do: ")
  mysquadinput2 = str(mysquadinput2)
  while mysquadinput2 != '1' and mysquadinput2 != '2' and mysquadinput2 != '3' and mysquadinput2 != '4':
    print("")
    print("Please enter a valid option!")
    print("")
    mysquadinput2 = input("Enter the number of what position you would like to edit: ")
    mysquadinput2 = str(mysquadinput2)
  if mysquadinput2 == '1':
    print("")
    print("All owned defenders:")
    print("")
    print("Starting Defender 1 - " + startingDefender1 + " - " + startingcountry1 + " - " + ovr1)
    print("Starting Defender 2 - " + startingDefender2 + " - " + startingcountry2 + " - " + ovr2)
    print("")
    f = open("defendername.txt", "r")
    e = open("defenderrating.txt", "r")
    g = open("defendercountry.txt", "r")
    linecount2 = 0
    ratingdict = {}
    for line in e:
      linecount2 = linecount2 + 1
      line = line.strip()
      ratingdict[linecount2] = line
    countrydict = {}
    linecount3 = 0
    for line in g:
      linecount3 = linecount3+1
      line = line.strip()
      countrydict[linecount3] = line
    linecount = 0
    for line in f:
      linecount = linecount+1
      line = line.strip()
      print(str(linecount) + " - " + line + " - " + countrydict[linecount] + " - " + ratingdict[linecount])
    f.close()
    e.close()
    g.close()
    time.sleep(0.5)
    print("")
    returntomysquad = input("Press enter to go back: ")
    print(allplayers())
  elif mysquadinput2 == '2':
    print("")
    print("All owned midfielders:")
    print("")
    print("Starting Midfielder 1 - " + startingMidfielder1 + " - " + startingcountry3 + " - " + ovr3)
    print("Starting Midfielder 2 - " + startingMidfielder2 + " - " + startingcountry4 + " - " + ovr4)
    print("")
    f = open("midfieldername.txt", "r")
    e = open("midfielderrating.txt", "r")
    g = open("midfieldercountry.txt", "r")
    linecount2 = 0
    ratingdict = {}
    for line in e:
      linecount2 = linecount2 + 1
      line = line.strip()
      ratingdict[linecount2] = line
    countrydict = {}
    linecount3 = 0
    for line in g:
      linecount3 = linecount3+1
      line = line.strip()
      countrydict[linecount3] = line
    linecount = 0
    for line in f:
      linecount = linecount+1
      line = line.strip()
      print(str(linecount) + " - " + line + " - " + countrydict[linecount] + " - " + ratingdict[linecount])
    f.close()
    e.close()
    g.close()
    time.sleep(0.5)
    print("")
    returntomysquad = input("Press enter to go back: ")
    print(allplayers())
  elif mysquadinput2 == '3':
    print("")
    print("All owned attackers:")
    print("")
    print("Starting Attacker 1 - " + startingAttacker1 + " - " + startingcountry5 + " - " + ovr5)
    print("Starting Attacker 2 - " + startingAttacker2 + " - " + startingcountry6 + " - " + ovr6)
    print("")
    f = open("attackername.txt", "r")
    e = open("attackerrating.txt", "r")
    g = open("attackercountry.txt", "r")
    linecount2 = 0
    ratingdict = {}
    for line in e:
      linecount2 = linecount2 + 1
      line = line.strip()
      ratingdict[linecount2] = line
    countrydict = {}
    linecount3 = 0
    for line in g:
      linecount3 = linecount3+1
      line = line.strip()
      countrydict[linecount3] = line
    linecount = 0
    for line in f:
      linecount = linecount+1
      line = line.strip()
      print(str(linecount) + " - " + line + " - " + countrydict[linecount] + " - " + ratingdict[linecount])
    f.close()
    e.close()
    g.close()
    time.sleep(0.5)
    print("")
    returntomysquad = input("Press enter to go back: ")
    print(allplayers())
  elif mysquadinput2 == '4':
    print(mysquadPage(coins))

# squad page function
def mysquadPage(coins):
  clear()
  global matches
  global chemistry
  global startingDefender1
  global startingDefender2
  global startingMidfielder1
  global startingMidfielder2
  global startingAttacker1
  global startingAttacker2
  global startingcountry1
  global startingcountry2
  global startingcountry3
  global startingcountry4
  global startingcountry5
  global startingcountry6
  global ovr1
  global ovr2
  global ovr3
  global ovr4
  global ovr5
  global ovr6
  global yourteamrating
  yourteamrating = int(yourteamrating)
  yourteamrating = (int(ovr1) + int(ovr2) + int(ovr3) + int(ovr4) + int(ovr5) + int(ovr6)) / 6
  yourteamrating = round(yourteamrating)
  f = open("yourteamrating.txt", "w")
  f.write(str(yourteamrating))
  f.close()
  chemistry = calculatechemistry()
  f = open("chem.txt", "w")
  f.write(str(chemistry))
  f.close()
  print("")
  print("MY SQUAD")
  print("")
  print("Team rating: " + str(yourteamrating) + " OVR")
  print("Team chemistry: " + str(chemistry) + "/55")
  print("")
  print("DEF - " + startingDefender1 + " - " + ovr1)
  print("DEF - " + startingDefender2 + " - " + ovr2)
  print("MID - " + startingMidfielder1 + " - " + ovr3)
  print("MID - " + startingMidfielder2 + " - " + ovr4)
  print("ATT - " + startingAttacker1 + " - " + ovr5)
  print("ATT - " + startingAttacker2 + " - " + ovr6)
  print("")
  print("Edit Starting lineup             - 1")
  print("View player information          - 2")
  print("View all owned players           - 3")
  print("Return to home                   - 4")
  print("")
  mysquadinput = input("Enter the number of what you would like to do: ")
  mysquadinput = str(mysquadinput)
  while mysquadinput != "1" and mysquadinput != "2" and mysquadinput != "3" and mysquadinput != "4":
    print("")
    print("Please enter a valid option!")
    print("")
    mysquadinput = input("Enter the number of what you would like to do: ")
    mysquadinput = str(mysquadinput)
  if mysquadinput == "1":
    clear()
    print("")
    print("1 - DEF - " + startingDefender1 + " - " + startingcountry1 + " - " + ovr1)
    print("2 - DEF - " + startingDefender2 + " - " + startingcountry2 +  " - " + ovr2)
    print("3 - MID - " + startingMidfielder1 + " - " + startingcountry3 +  " - " + ovr3)
    print("4 - MID - " + startingMidfielder2 + " - " + startingcountry4 +  " - " + ovr4)
    print("5 - ATT - " + startingAttacker1 + " - " + startingcountry5 +  " - " + ovr5)
    print("6 - ATT - " + startingAttacker2 + " - " + startingcountry6 +  " - " + ovr6)
    print("")
    print("e - Return to My Squad")
    print("")
    mysquadinput2 = input("Enter the number of what position you would like to edit: ")
    mysquadinput2 = str(mysquadinput2)
    while mysquadinput2 != '1' and mysquadinput2 != '2' and mysquadinput2 != '3' and mysquadinput2 != '4' and mysquadinput2 != '5' and mysquadinput2 != '6' and mysquadinput2 != 'e':
      print("")
      print("Please enter a valid option!")
      print("")
      mysquadinput2 = input("Enter the number of what position you would like to edit: ")
      mysquadinput2 = str(mysquadinput2)
    if mysquadinput2 == '1':
      print("")
      f = open("defendername.txt", "r")
      e = open("defenderrating.txt", "r")
      linecount2 = 0
      ratingdict = {}
      for line in e:
        linecount2 = linecount2 + 1
        line = line.strip()
        ratingdict[linecount2] = line
      linecount = 0
      for line in f:
        linecount = linecount+1
        line = line.strip()
        print(str(linecount) + " - " + line + " - " + ratingdict[linecount])
      f.close()
      e.close()
      f = open("defendername.txt", "r")
      content = f.read()
      f.close()
      print("")
      if len(content) == 0:
        time.sleep(2)
        print("ERROR: You own no other defenders")
        time.sleep(2)
        print(mysquadPage(coins))
      while True:
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        try:
          mysquadinput3 = int(mysquadinput3)
          break
        except ValueError:
          print("")
          print("Please enter a valid option!")
          print("")
      while mysquadinput3 < 1 or mysquadinput3 > linecount:
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        mysquadinput3 = int(mysquadinput3)
      mysquadinput3 = str(mysquadinput3)
      sd1(mysquadinput3)
      print(mysquadPage(coins))
    elif mysquadinput2 == '2':
      print("")
      e = open("defenderrating.txt", "r")
      linecount2 = 0
      ratingdict = {}
      for line in e:
        linecount2 = linecount2 + 1
        line = line.strip()
        ratingdict[linecount2] = line
      e.close()
      f = open("defendername.txt", "r")
      linecount = 0
      for line in f:
        linecount = linecount+1
        line = line.strip()
        print(str(linecount) + " - " + line + " - " + ratingdict[linecount])
      f.close()
      f = open("defendername.txt", "r")
      content = f.read()
      f.close()
      print("")
      if len(content) == 0:
        time.sleep(2)
        print("ERROR: You own no other defenders")
        time.sleep(2)
        print(mysquadPage(coins))
      while True:
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        try:
          mysquadinput3 = int(mysquadinput3)
          break
        except ValueError:
          print("")
          print("Please enter a valid option!")
          print("")
      while mysquadinput3 < 1 or mysquadinput3 > linecount:
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        mysquadinput3 = int(mysquadinput3)
      mysquadinput3 = str(mysquadinput3)
      sd2(mysquadinput3)
      print(mysquadPage(coins))
    elif mysquadinput2 == '3':
      print("")
      f = open("midfieldername.txt", "r")
      e = open("midfielderrating.txt", "r")
      linecount2 = 0
      ratingdict = {}
      for line in e:
        linecount2 = linecount2 + 1
        line = line.strip()
        ratingdict[linecount2] = line
      linecount = 0
      for line in f:
        linecount = linecount+1
        line = line.strip()
        print(str(linecount) + " - " + line + " - " + ratingdict[linecount])
      f.close()
      e.close()
      f = open("midfieldername.txt", "r")
      content = f.read()
      f.close()
      print("")
      if len(content) == 0:
        time.sleep(2)
        print("ERROR: You own no other midfielders")
        time.sleep(2)
        print(mysquadPage(coins))
      while True:
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        try:
          mysquadinput3 = int(mysquadinput3)
          break
        except ValueError:
          print("")
          print("Please enter a valid option!")
          print("")
      while mysquadinput3 < 1 or mysquadinput3 > linecount:
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        mysquadinput3 = int(mysquadinput3)
      mysquadinput3 = str(mysquadinput3)
      sm1(mysquadinput3)
      print(mysquadPage(coins))
    elif mysquadinput2 == 'e':
      print(mysquadPage(coins))
    elif mysquadinput2 == '4':
      print("")
      f = open("midfieldername.txt", "r")
      e = open("midfielderrating.txt", "r")
      linecount2 = 0
      ratingdict = {}
      for line in e:
        linecount2 = linecount2 + 1
        line = line.strip()
        ratingdict[linecount2] = line
      linecount = 0
      for line in f:
        linecount = linecount+1
        line = line.strip()
        print(str(linecount) + " - " + line + " - " + ratingdict[linecount])
      f.close()
      e.close()
      f = open("midfieldername.txt", "r")
      content = f.read()
      f.close()
      print("")
      if len(content) == 0:
        time.sleep(2)
        print("ERROR: You own no other midfielders")
        time.sleep(2)
        print(mysquadPage(coins))
      while True:
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        try:
          mysquadinput3 = int(mysquadinput3)
          break
        except ValueError:
          print("")
          print("Please enter a valid option!")
          print("")
      while mysquadinput3 < 1 or mysquadinput3 > linecount:
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        mysquadinput3 = int(mysquadinput3)
      mysquadinput3 = str(mysquadinput3)
      sm2(mysquadinput3)
      print(mysquadPage(coins))
    elif mysquadinput2 == '5':
      f = open("attackername.txt", "r")
      e = open("attackerrating.txt", "r")
      linecount2 = 0
      ratingdict = {}
      for line in e:
        linecount2 = linecount2 + 1
        line = line.strip()
        ratingdict[linecount2] = line
      linecount = 0
      for line in f:
        linecount = linecount+1
        line = line.strip()
        print(str(linecount) + " - " + line + " - " + ratingdict[linecount])
      f.close()
      e.close()
      f = open("attackername.txt", "r")
      content = f.read()
      f.close()
      print("")
      if len(content) == 0:
        time.sleep(2)
        print("ERROR: You own no other attackers")
        time.sleep(2)
        print(mysquadPage(coins))
      while True:
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        try:
          mysquadinput3 = int(mysquadinput3)
          break
        except ValueError:
          print("")
          print("Please enter a valid option!")
          print("")
      while mysquadinput3 < 1 or mysquadinput3 > linecount:
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        mysquadinput3 = int(mysquadinput3)
      mysquadinput3 = str(mysquadinput3)
      sa1(mysquadinput3)
      print(mysquadPage(coins))
    elif mysquadinput2 == '6':
      f = open("attackername.txt", "r")
      e = open("attackerrating.txt", "r")
      linecount2 = 0
      ratingdict = {}
      for line in e:
        linecount2 = linecount2 + 1
        line = line.strip()
        ratingdict[linecount2] = line
      linecount = 0
      for line in f:
        linecount = linecount+1
        line = line.strip()
        print(str(linecount) + " - " + line + " - " + ratingdict[linecount])
      f.close()
      e.close()
      f = open("attackername.txt", "r")
      content = f.read()
      f.close()
      print("")
      if len(content) == 0:
        time.sleep(2)
        print("ERROR: You own no other attackers")
        time.sleep(2)
        print(mysquadPage(coins))
      while True:
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        try:
          mysquadinput3 = int(mysquadinput3)
          break
        except ValueError:
          print("")
          print("Please enter a valid option!")
          print("")
      while mysquadinput3 < 1 or mysquadinput3 > linecount:
        print("")
        print("Please enter a valid option!")
        print("")
        mysquadinput3 = input("Enter the number of what player you would like to replace: ")
        mysquadinput3 = int(mysquadinput3)
      mysquadinput3 = str(mysquadinput3)
      sa2(mysquadinput3)
      print(mysquadPage(coins))
  elif mysquadinput == "2":
    print(viewplayerPage(coins))
  elif mysquadinput == "3":
    print(allplayers())
  elif mysquadinput == "4":
    print(homePage(coins))

# start the program
print("CREATED BY:")
time.sleep(0.3)
print("WILLIAM HE")
time.sleep(0.3)
print("JADRIEN JUDE LAWRENCE")
time.sleep(1)
clear()
print("")
print("FOOTBALL MANAGER")
time.sleep(0.3)
print("")
print("Welcome to Football Manager!")
print("")
time.sleep(0.3)
yourteamname = input("Please enter your team name: ")
f = open("username.txt", "a")
f.close()
f = open("username.txt", "r")
username = f.read()
f.close()
if yourteamname == username:
  password = input("Please enter your password: ")
  f = open("password.txt", "r")
  previouspassword = f.read()
  while password != previouspassword:
    print("ERROR: The password you typed was incorrect")
    password = input("Please enter your password: ")
  time.sleep(1)
  print("")
  print("Logging in...")
  time.sleep(2)
  print("")
  print("Welcome back, " + yourteamname + "!")
  #saving coins earnt from previously playing
  f = open("coins.txt", "r")
  coinString = f.read()
  coins = int(coinString)
  f.close()
  #loading starting team
  f = open("startingdefender1.txt", "r")
  startingDefender1 = f.read()
  f.close()
  f = open("startingdefender2.txt", "r")
  startingDefender2 = f.read()
  f.close()
  f = open("startingmidfielder1.txt", "r")
  startingMidfielder1 = f.read()
  f.close()
  f = open("startingmidfielder2.txt", "r")
  startingMidfielder2 = f.read()
  f.close()
  f = open("startingattacker1.txt", "r")
  startingAttacker1 = f.read()
  f.close()
  f = open("startingattacker2.txt", "r")
  startingAttacker2 = f.read()
  f.close()
  f = open("ovr1.txt", "r")
  ovr1 = f.read()
  f.close()
  f = open("ovr2.txt", "r")
  ovr2 = f.read()
  f.close()
  f = open("ovr3.txt", "r")
  ovr3 = f.read()
  f.close()
  f = open("ovr4.txt", "r")
  ovr4 = f.read()
  f.close()
  f = open("ovr5.txt", "r")
  ovr5 = f.read()
  f.close()
  f = open("ovr6.txt", "r")
  ovr6 = f.read()
  f.close()
  f = open("startingcountry1.txt", "r")
  startingcountry1 = f.read()
  f.close()
  f = open("startingcountry2.txt", "r")
  startingcountry2 = f.read()
  f.close()
  f = open("startingcountry3.txt", "r")
  startingcountry3 = f.read()
  f.close()
  f = open("startingcountry4.txt", "r")
  startingcountry4 = f.read()
  f.close()
  f = open("startingcountry5.txt", "r")
  startingcountry5 = f.read()
  f.close()
  f = open("startingcountry6.txt", "r")
  startingcountry6 = f.read()
  f.close()
  f = open("yourteamrating.txt", "r")
  yourteamratingstring = f.read()
  yourteamrating = int(yourteamratingstring)
  f.close()
  f = open("lastteam.txt", "r")
  lastteam = f.read()
  f.close()
  f = open("chem.txt", "r")
  chemistry = f.read()
  f.close()
  f = open("league.txt", "r")
  league = f.read()
  league = int(league)
  f.close()
  f = open("points.txt", "r")
  points = f.read()
  points = int(points)
  f.close()
  f = open("game.txt", "r")
  game = f.read()
  game = int(game)
  f.close()
  f = open("wins.txt", "r")
  wins = f.read()
  wins = int(wins)
  f.close()
  f = open("draws.txt", "r")
  draws = f.read()
  draws = int(draws)
  f.close()
  f = open("losses.txt", "r")
  losses = f.read()
  losses = int(losses)
  f.close()
  f = open("matches.txt", "r")
  matches = f.read()
  matches = int(matches)
  f.close()

else:
  time.sleep(1)
  print("")
  newaccount = input("WARNING: Creating a new account will delete all your previous progress! Are you sure you want to continue? (y/n): ")
  while newaccount != "y" and newaccount != "n":
    print("")
    print("Please enter a valid option!")
    print("")
    newaccount = input("WARNING: Creating a new account will delete all your previous progress! Are you sure you want to continue? (y/n): ")
  if newaccount == "n":
    clear()
    sys.exit()
  print()
  password = input("Please create a password: ")
  confirmpassword = input("Please confirm your password: ")
  while password != confirmpassword:
    print("ERROR: The passwords you typed do not match")
    password = input("Please create a password: ")
    confirmpassword = input("Please confirm your password: ")
  time.sleep(1)
  print("")
  print("Creating new account...")
  time.sleep(2)
  print("")
  print("Account created!")
  time.sleep(1)
  f = open("password.txt", "w")
  f.write(password)
  print("")
  print("Welcome to Football Manager, " + yourteamname + "!")
  f = open("startingdefender1.txt", "w")
  f.write("Y.Randolph")
  f.close()
  startingDefender1 = "Y.Randolph"
  f = open("startingdefender2.txt", "w")
  f.write("R.Ito")
  f.close()
  startingDefender2 = "R.Ito"
  f = open("startingmidfielder1.txt", "w")
  f.write("V.Williams")
  f.close()
  startingMidfielder1 = "V.Williams"
  f = open("startingmidfielder2.txt", "w")
  f.write("Q.Phillips")
  f.close()
  startingMidfielder2 = "Q.Phillips"
  f = open("startingattacker1.txt", "w")
  f.write("G.Thomas")
  f.close()
  startingAttacker1 = "G.Thomas"
  f = open("startingattacker2.txt", "w")
  f.write("P.Muller")
  f.close()
  startingAttacker2 = "P.Muller"
  f = open("startingcountry1.txt", "w")
  f.write('England')
  f.close()
  startingcountry1 = "England"
  f = open("startingcountry2.txt", "w")
  f.write('England')
  f.close()
  startingcountry2 = "England"
  f = open("startingcountry3.txt", "w")
  f.write('England')
  f.close()
  startingcountry3 = "England"
  f = open("startingcountry4.txt", "w")
  f.write('England')
  f.close()
  startingcountry4 = "England"
  f = open("startingcountry5.txt", "w")
  f.write('England')
  f.close()
  startingcountry5 = "England"
  f = open("startingcountry6.txt", "w")
  f.write('England')
  f.close()
  startingcountry6 = "England"
  f = open("ovr1.txt", "w")
  f.write('52')
  f.close()
  ovr1 = '52'
  f = open("ovr2.txt", "w")
  f.write('51')
  f.close()
  ovr2 = '51'
  f = open("ovr3.txt", "w")
  f.write('56')
  f.close()
  ovr3 = '56'
  f = open("ovr4.txt", "w")
  f.write('50')
  f.close()
  ovr4 = '50'
  f = open("ovr5.txt", "w")
  f.write('52')
  f.close()
  ovr5 = '52'
  f = open("ovr6.txt", "w")
  f.write('50')
  f.close()
  ovr6 = '50'
  yourteamrating = 52
  f = open("yourteamrating.txt", "w")
  yourteamratingstring = str(yourteamrating)
  f.write(yourteamratingstring)
  f.close()
  f = open("lastteam.txt", "w")
  f.write("False")
  f.close()
  lastteam = "False"
  f = open("username.txt", "w")
  f.write(yourteamname)
  f.close()
  f = open("attackercountry.txt", "w")
  f.close()
  f = open("attackername.txt", "w")
  f.close()
  f = open("attackerrating.txt", "w")
  f.close()
  f = open("midfieldercountry.txt", "w")
  f.close()
  f = open("midfieldername.txt", "w")
  f.close()
  f = open("midfielderrating.txt", "w")
  f.close()
  f = open("defendercountry.txt", "w")
  f.close()
  f = open("defendername.txt", "w")
  f.close()
  f = open("defenderrating.txt", "w")
  f.close()
  f = open("chem.txt", "w")
  f.write('55')
  f.close()
  coins = 1000
  coinString = str(coins)
  f = open("coins.txt", "w")
  f.write(coinString)
  f.close()
  league = 4
  f = open("league.txt", "w")
  f.write(str(league))
  f.close()
  points = 0
  f = open("points.txt", "w")
  f.write(str(points))
  f.close()
  game = 10
  f = open("game.txt", "w")
  f.write(str(game))
  f.close()
  f = open("matchhistory.txt", "w")
  f.close()
  f = open("wins.txt", "w")
  f.write('0')
  f.close()
  f = open("losses.txt", "w")
  f.write('0')
  f.close()
  f = open("draws.txt", "w")
  f.write('0')
  f.close()
  f = open("matches.txt", "w")
  f.write('0')
  f.close()
  wins = 0
  draws = 0
  losses = 0
  matches = 0
print("")
time.sleep(2.5)
print(homePage(coins))
