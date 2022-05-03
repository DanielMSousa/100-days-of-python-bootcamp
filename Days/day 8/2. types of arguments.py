def greet_with_name(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet_with_name('Daniel', 'Brazil')

#these arguments are positional, they're based in the position

greet_with_name(location='China', name='Jennifer')

#these arguments are keyword arguments, their positions doesn't matter