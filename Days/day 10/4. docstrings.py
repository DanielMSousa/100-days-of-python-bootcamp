# function documentation is something that tells you how to use a certain function
#you'll use a docstring on the first line after the function declaration using 3 quotations symbols

def format_name(f_name, l_name):
  """Take a first and lastname and format it to return the title case version of the name"""
  if(f_name == "" or l_name == ""):
    return
  full_name = f'{f_name.title()} {l_name.title()}'
  return full_name

print(format_name("MiDas", "EnÉiAS"))

"""You can also
use this as a multiline comment"""