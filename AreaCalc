###Something to do with calculating the area of a shape using maths stuffs###

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Calculation commencing ..."
print "Current Time: %.2d/%.2d/%.2d %.2d:%.2d" % (now.month, now.day, now.year, now.hour, now.minute)

sleep (1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("\nEnter C for Circle, R for Rectangle, S for Square or T for Triangle, then hit <Enter>: ")

option = option.upper()

if option == "C":
  radius = float(raw_input("Please provide the radius of the circle: "))
  area = pi * (radius * radius)
  print "The pie is baking...\n"
  sleep(1)
  print "The area of the circle is %.2f \n\n%s" % (area, hint)
elif option == "T":
  base = float(raw_input("Please provide the base of the triangle: "))
  height = float(raw_input("Provide the height of the triangle: "))
  area = base * height / 2
  print "Uni Bi Tri...\n"
  sleep(1)
  print "The area of the triangle is %.2f \n\n%s" % (area, hint)
elif option == "S":
  height = float(raw_input("Provide the height of the square: "))
  area = height * height
  print "Ensquaring...\n"
  sleep(1)
  print "The area of the square is %.2f \n\n%s" % (area, hint)
elif option == "R":
  width = float(raw_input("Provide the width of the rectangle: "))
  length = float(raw_input("Provide the length of the rectangle: "))
  area = width * length
  print "Juan Toe Free...\n"
  sleep(1)
  print "The area of the rectangle is %.2f \n\n%s" % (area, hint)
else:
  print "You have entered an invalid value. The program will exit."
