#functions with outputs
# Having an output doesn't imply on having an input

def format_name(f_name, l_name):
  name = f'{f_name.title()} {l_name.title()}'
  return name

n = format_name('aNgELa', 'yU')

print(n)
