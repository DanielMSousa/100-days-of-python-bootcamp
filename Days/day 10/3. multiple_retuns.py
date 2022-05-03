def format_name(f_name, l_name):
  #you can return nothing (None)
  if(f_name == "" or l_name == ""):
    return
  full_name = f'{f_name.title()} {l_name.title()}'
  return full_name

n = format_name('aNgELa', 'yU')

print(n)
