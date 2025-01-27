# password validator
""" must follow:
 - Minimum length is 5;
 - Maximum length is 10;
 - Should contain at least one number;
 - Should contain at least one special character (such as &, +, @, $, #, %, etc.);
 - Should not contain spaces """ 
 
prompt = str(input("Enter a valid password. Password must be 5-10 characters long with at least 1 number and 1 special character (such &, +, @, $, #, %, etc.) No spaces are allowed.\n \n"))
# validate
if len(prompt) > 10:
  print("Error! Password must be less than 10 characters long.")
  while len(prompt) > 10:
    prompt = str(input("Enter a valid password. Password must be 5-10 characters long with at least 1 number and 1 special character (such &, +, @, $, #, %, etc.) No spaces are allowed."))
  if len(prompt) < 5:
    print("Error! Password must be at least 5 characters long.")
    while len(prompt) < 5:
      prompt = str(input("Enter a valid password. Password must be 5-10 characters long with at least 1 number and 1 special character (such &, +, @, $, #, %, etc.) No spaces are allowed."))
    if num_check(prompt) == False:
      print("Error! Password must include at least 1 number.")
      while num_check(prompt) == False:
        prompt = str(input("Enter a valid password. Password must be 5-10 characters long with at least 1 number and 1 special character (such &, +, @, $, #, %, etc.) No spaces are allowed."))
      if spec_check(prompt) == False:
        print("Error! Password must include at least 1 special character.")
        while spec_check(prompt) == False:
          prompt = str(input("Enter a valid password. Password must be 5-10 characters long with at least 1 number and 1 special character (such &, +, @, $, #, %, etc.) No spaces are allowed."))
        if spec_check(prompt) == False:
          print("Error! Password must not contain whitespaces.")
          while spec_check(prompt) == False:
            prompt = str(input("Enter a valid password. Password must be 5-10 characters long with at least 1 number and 1 special character (such &, +, @, $, #, %, etc.) No spaces are allowed."))
else:
  print("Password validated.")
  
 
# function to check for numbers in password, using loop
def num_check(input):
  i = 0
  for i in prompt[len(input) - 1]:
    if prompt[i] == "0" or "1" or "2" or "3" or "4" or "5 or 6" or "7" or "8" or "9":
      num = True
      return num
    else:
      num = False
      return num
      
     
# function to check for special characters in password, using loop
def spec_check(input):
  i = 0
  for i in prompt[len(input) - 1]:
    if prompt[i] == "@" or "!" or "$" or "&" or "?" or ":" or "#" or "/" or "]" or "[" or "}" or "{" or "%" or ";" or "^" or "*" or "+" or "=" or "<" or "~" or "_":
      spec = True
      return spec
    else:
      spec = False
      return spec
      
     
# function to check for whitespace in password, using loop
def space_check(input):
  i = 0
  for i in prompt[len(input) - 1]:
    if prompt[i] == " ":
      space = True
      return space
    else:
      space = False
      return space
