import random, time, os

def char1():
  a = input('\033[33mWhat is your Character name: \033[0m')
  print()
  b = input('\033[34mWhat is your character type (human, imp, wizard, elf): \033[0m').lower()
  print()
  return a, b

def Health():
  a = random.randint(1, 6)
  b = random.randint(1, 12)
  c = ((a*b)/2) + 10
  return c

def Strength():
  a = random.randint(1, 6)
  b = random.randint(1, 12)
  c = ((a*b)/2) + 12
  return c

while True:
  print('\033[35mCharacter Builder\033[0m')
  time.sleep(2)
  print()
  print(f'\033[32m{char1()[0]}')
  time.sleep(1)
  print(f'''
HEALTH: {Health()}
STRENGTH: {Strength()}
  \033[0m''')
  time.sleep(2)
  print('My your name go down in Legend...')
  time.sleep(1)
  print()
  ask = input('Want to generate stats for another character? y/n: ').lower()
  print()
  if ask == 'y':
    os.system('clear')
    continue
  else:
    print('Bye! Do Take of yourself.😊')
    break