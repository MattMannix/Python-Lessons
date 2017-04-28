"""A dice based number guessing game"""

from random import randint
from time import sleep

def get_user_guess ():
  user_guess = int(raw_input("Guess the total of the dice roll: "))
  return user_guess

def roll_dice (number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible dice value is..." + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  
  if user_guess > max_val:
    print "You guessed higher than the maximum value"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first dice is: %d" % first_roll
    print "The second dice is: %d" % second_roll
    sleep(1)
    total_value = first_roll + second_roll
    print "The total rolled value is: %d" % total_value
    print "Result..."
    sleep(1)
    if user_guess > total_value:
      print "Congratulations!"
      return
    else:
      print "Loser!"
      return
    
roll_dice(6)
