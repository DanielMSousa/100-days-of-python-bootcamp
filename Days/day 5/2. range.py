fruits = ['apple', 'peach', 'pear']

#range(a, b, c) -> generates a sequence between a and b (b not included) with a step of c, if you only inserts a number it goes between 0 and this number

acc = 0
for number in range(1, 101):
  acc += number

print(acc)