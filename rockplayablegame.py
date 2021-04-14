import random
global alive

alive = True
print("welcome to very fun rpg")
print("enter the commands specified in order to do stuff")
print("if you end a turn with negative health, you lose")
print("when you have negative health, you have one more turn to try and heal")
print("enjoy")
name = input("enter your name")
cheatactive = input("cheatcode:")
movecount = 0
def stats():
  print("name:",name)
  print("level:",level)
  print("gold:",gold)
  print("health:",health)
  print("heal strength:",heals)
  print("attack:",attack)
  print("defense:",defense)
  print("___________")

def enemystats():
  global enemyh
  global enemya
  enemyh = 15 + (level*4)
  enemya = 5 + (level*2)

def hardenemystats():
  global henemyh
  global henemya
  henemyh = 25 + (level*5)
  henemya = 5 + (level*3)

def game():
  enemystats()
  hardenemystats()
  global level
  global attack
  global gold
  global health
  global y
  global alive
  global name
  global heals
  global defense
  global movecount
  if health <= 0:
    health = -1000
  def fight():
    global enemyh
    global gold
    global charge
    global enemya
    global health
    global attack
    global level
    global alive
    global heals
    global defense
    z = ""
    print("!!!!!!!!!!!!!")
    print("enemys health:",enemyh)
    print("enemys attack:",enemya)
    print("/////////////")
    print("your health:",health)
    print("your attack:",attack)
    print("special charge:",charge*10,"%")
    print("choose a fight command")
    if health <= 0:
      health = -10000
      game()
    x = input("attack,special,heal,defend")
    print("-----action-----")
    if x == ("special"):
          if charge >= 10:
              enemyh = enemyh - (attack*10)
              print("did",attack*10,"damage")
              charge -= 10
          else:
              print("not enough charge")
    if x == ("attack"):
      enemyh = enemyh - attack
      print("did",attack,"damage")
      charge += 1
    if x == ("heal"):
      health += heals
      print("healed",heals,"health")
      charge += 1
    if enemyh <= 0:
      level += 1
      attack += 2
      health += 5
      heals += 1
      defense += 1
      gold += 150
      charge = 0
      print("defeated enemy, +150 gold, +1 level")
    else:
      z = random.randint(1,10)
      if z == 1 or z == 2 or z == 3 or z == 4:
        print("----> enemy heals")
        enemyh += enemya/2
        print("enemy healed",enemya/2,"health")
        charge += 3
      if z == 5 or z == 6 or z == 7 or z == 8 or z == 9:
        print("----> enemy attacks")
        if x == ("defend"):
          health = health - (enemya - defense)
          print("enemy did",enemya - defense,"damage")
          charge += 3
        else:
          health = health - enemya
          print("enemy did", enemya,"damage")
      if z == 10:
        print("----> enemy breakdances")
      print("==========================")
      fight()
  def hardfight():
    global henemyh
    global henemya
    global health
    global gold
    global attack
    global level
    global charge
    global alive
    global heals
    global defense
    z = ""
    print("(!)(!)(!)(!)(!)")
    print("enemys health:",henemyh)
    print("enemys attack:",henemya)
    print(">>>>>>>>><<<<<<<")
    print("your health:",health)
    print("your attack:",attack)
    print("special charge:",charge*10,"%")
    print("choose a fight command")
    print("-----action-----")
    if health <= 0:
      health = -10000
      game()
    x = input("attack,special,heal,defend")
    if x == ("special"):
      if charge >= 10:
        henemyh = henemyh - (attack*10)
        print(attack*10)
        charge -= 10
      else:
        print("not enough charge")
    if x == ("attack"):
      henemyh = henemyh - attack
      charge += 1
    if x == ("heal"):
      health += heals/2
      print("healed",heals/2,"health")
      charge += 1
    if henemyh <= 0:
      level += 2
      attack += 4
      health += 10
      heals += 2
      defense += 2
      gold += 250
      print("difficult enemy defeated, + 250 gold, + 2 levels")
    else:
      z = random.randint(1,10)
      if z == 1 or z == 2 or z == 3 or z == 4 or z == 5:
        print("----> enemy heals")
        henemyh = henemyh + henemya
        print("enemy healed",henemya,"health")
        charge += 3
      if z == 6 or z == 7 or z == 8 or z == 9 or z:
        print("----> enemy attacks")
        if x == ("defend"):
          health = health - (henemya - defense)
          charge += 3
          print("enemy did",henemya - defense,"damage")
        else:
          health = health - (henemya*2)
          print("enemy did",henemya*2,"damage")
      if z == 10:
        print("----> difficult enemy does a pushup")
      print("================================")
      hardfight()
  if health <= 0:
    alive = False
  print("enter a command,",name)
  y = input("(move,stats,heal,attack,sleep,beg,end)")
  print("<><><><><><><>")
  if y == ("end"):
    health = -10000
  if y == ("attack"):
    u = random.randint(1,5)
    if u == 1:
      print("you hit a goose flying by, i would add a level, but you kinda tripped when you swang at it")
    if u == 2:
      print("you punch a rock, health - 1")
      health -= 1
    if u == 3:
      print("you swing at a random monster doing his laundry and then boom")
      fight()
    if u == 4:
      print("you happen to slice open a locked treasure chest and get a couple of gold")
      gold += 20
      print("gold is now",gold)
    if u == 5:
      print("you swing your weapon at the ground and it hits a chill rock, not cool dude")
  if y == ("sleep"):
    print("you go to sleep and reset your health")
    if health < 35:
      health = 20 + (level*5)
      print("health restored to default")
    else:
      print("you awoke as usual")
      health += heals
  if y == ("move"):
    movecount += 1
    event = random.randint(1,13)
    if event == 1:
      print(":O :O :O :O")
      print("found a cool rock, level up")
      level += 1
      attack += 2
      health += 5
      heals += 1
      defense += 1
    if event == 2:
      print(">:( >:( >:( >:(")
      print("found an enemy")
      fight()
    if event == 3:
      print("you find a neat little pond and sit for a while, heal strength + 1")
      print("heal strenght is now",heals)
      heals += 1
    if event == 4:
      print("you were attacked on your trip onwards, health - 5")
      health -= 5
    if event == 5:
      print("you moved a few steps, then gave up")
    if event == 6:
      print("you ate at a cool looking hotdog stand, health + 5")
      health += 5
    if event == 7:
      print("you got a booboo and put a bandaid on :< defense + 1")
      print("defense is now",defense)
      defense += 1
    if event == 8:
      print("a bandaid fell off :< defense - 1")
    if event == 9:
      print("a very angry enemy attacks you")
      hardfight()
    if event == 10:
      print("found a coin on the ground")
      print("gold + 50")
      gold += 50
      print("gold is now",gold)
    if event == 11:
      print("you happened upon a cool store, choose what you'll buy")
      print("+attack [250 gold]")
      print("+defense [200 gold]")
      print("+strength of heal [300 gold]")
      print("+level [500 gold]")
      print("+health pot [1000 gold]")
      print("work here [+200 gold]")
      print("nothing")
      print("type in first letter of what you want")
      print("total gold:",gold)
      w = input("a,d,s,l,h,w,n")
      if w == ("a"):
        if gold >= 250:
          print("bought the attack up, attack + 1")
          attack += 1
          gold -= 250
        else:
          print("cant afford, you left")
      if w == ("d"):
        if gold >= 200:
          defense += 1
          print("bought the defense up, defense + 1")
          gold -= 200
        else:
          print("cant afford, you left")
      if w == ("s"):
        if gold >= 300:
          heals += 1
          print("bought the heal strength up, heal strength + 1")
          gold -= 300
        else:
          print("cant afford, you left")
      if w == ("l"):
        if gold >= 500:
          level += 1
          print("bought a level up, level + 1")
          gold -= 500
        else:
          print("cant afford, you left")
      if w == ("h"):
        if gold >= 1000:
          health += 400
          print("bought the healing potion, health + 100")
          gold -= 1000
        else:
          print("cant afford, you left")
      if w == ("w"):
        gold += 200
        print("the cool store owner paid you 200 gold, and welcomed you to return")
      if w == ("n"):
        print("you left the store")
    if event == 12:
      print("you get an error from playing this game and lose 20 health")
      health -= 20
    if event == 13:
      print("you happen to find a cheat code for your favorite 2d text adventure program")
      print("?????????????")
      k = random.randint(1,6)
      if k == 1:
        print("rich: makes you super rich")
      if k == 2:
        print("poor: makes you a realistic character")
      if k == 3:
        print("levelup: gives you 1000 levels")
      if k == 4:
        print("yes: makes your first turn really annoying")
      if k == 5:
        print("rock: makes you an original character")
      if k == 6:
        print("coolrock: makes you very strong")
  if y == ("stats"):
    print("_______")
    stats()
  if y == ("heal"):
    if health <= 0:
      health = -10000
    print("health:",health)
    health += heals
    print("health:",health)
  if y == ("beg"):
    d = random.randint(1,10)
    if d == 1 or d == 2 or  d == 3:
      print("you haggle at some old people for spare change, you get 10 gold")
      gold += 10
      print("gold is now",gold)
    if d == 4 or d == 5:
      print("you find a real beggar and give him 5 gold")
      if gold >= 5:
        gold -= 5
        print("gold is now",gold)
      else:
        print("but you didnt have enough money and instead sat down next to him")
        print("beggar: so,",name,",living the dream huh, lucky you can actually go out and earn money")
        print("do you feel like this is fair?")
        res = input("answer:")
        if res == ("yes"):
          print("beggar: and thats why nothing will ever change")
        if res == ("no"):
          print("beggar: and theres nothing anyone can do about it")
        else:
          print("interesting choice,",name,",but in the end, im just a response to your choices anyways")
    if d == 6 or d == 7 or d == 8 or d == 9:
      print("you couldnt find anyone")
    if d == 10:
      print("a rich noble decided you were annoying them and gave you 300 gold")
      gold += 300
      print("gold is now",gold,"and you are sorta evil")
level = 1
if cheatactive == ("rock"):
  print("name is original now")
  name = ("rock")
attack = 9
if cheatactive == ("coolrock"):
  print("infinite attack :)")
  name = ("sharp rock")
  attack = 100000
health = 25
if cheatactive == ("yes"):
  print("okay never said it was good")
  print("health is 1 from start")
  name = ("person who chose yes")
  health = 1
heals = 6
gold = 200
if cheatactive == ("rich"):
  print("you were born in a moderately wealthy family")
  gold = 10000
  name = ("rich rock")
defense = 7
if cheatactive == ("levelup"):
  print("you got it")
  level = 1000
  attack = 1000
  health = 1000
  heals = 1000
  defense = 1000
  gold = 10000000
  name = ("big rock")
charge = 0
if cheatactive == ("poor"):
  gold = -10000
  print("you live in america now")
while alive == True:
  game()
print("your health was below 1,",name)
stats()
print(" :< :< :< :< :< ")
print("TOTAL MOVES:",movecount)
print("reset game to play again")
