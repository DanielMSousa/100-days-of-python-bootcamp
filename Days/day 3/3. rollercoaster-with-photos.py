print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0;

if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Child tickets are 5$")
    bill = 5
  elif age <= 18:
    print("Youth tickets are 7$")
    bill = 7
  else:
    print("Adults tickets are 12$")
    bill = 12
  
  wants_photos = input("Do you want a photo taken? Y/N")
  if(wants_photos == 'Y'):
    print("")
    bill += 3
  
  print(f"Your final bill is {bill}")
else:
  print("Sorry, you have to grow taller before you can ride")


