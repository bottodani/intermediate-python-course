import random

def main():
  dice_rolls = int(input("How many dice would you like to roll?"))
  dice_size = int(input("Hány oldalú legyen a kocka?"))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Ez nagy baj!')
    elif roll == dice_size:
      print(f"You rolled a {roll}! Gratulálunk!")
    else:
      print(f'You rolled a {roll}')
  print(f"Összesen: {dice_sum}")

if __name__== "__main__":
  main()