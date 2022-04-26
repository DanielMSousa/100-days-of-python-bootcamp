# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_score = name1.lower().count('t')
true_score += name2.lower().count('t')
true_score += name1.lower().count('r')
true_score += name2.lower().count('r')
true_score += name1.lower().count('u')
true_score += name2.lower().count('u')
true_score += name1.lower().count('e')
true_score += name2.lower().count('e')

love_score = name1.lower().count('l')
love_score += name2.lower().count('l')
love_score += name1.lower().count('o')
love_score += name2.lower().count('o')
love_score += name1.lower().count('v')
love_score += name2.lower().count('v')
love_score += name1.lower().count('e')
love_score += name2.lower().count('e')

score = int(str(true_score) + str(love_score))

if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score > 40 and score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

