

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

print(
programming_dictionary["Bug"])

#adding an element to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

#Changing a value
programming_dictionary["Bug"] = "A moth in yout computer"

print(programming_dictionary["Bug"])
#creating an empty dictionary:
empty_dictionary = {}

#wiping an existing dictionary
#programming_dictionary= {}

#Loop through a dictionary:
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])