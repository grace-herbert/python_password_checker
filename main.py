import re

username = input("Please enter a username: ")

print('Please enter a password, it must be at least 11 characters long, have 1 number, 1 Capital letter, 1 lowercase letter and one symbol')

pwd = input('Please enter a password: ')

reenter_pwd = input(' Please re-enter a password: ')

pwd_length = len(pwd)

pwd_hidden = '*' * pwd_length

if(len(pwd) >= 11):
  pwd_len = True
else: pwd_len = False
  
if(pwd == reenter_pwd):
  pwd_match = True
else:pwd_match = False

if(re.search("[0-9]", pwd) and re.search("[A-Z]", pwd) and re.search("[a-z]", pwd) and re.search("[!%*^$]", pwd) ):
  format_check = True;
else:format_check = False

if((pwd_len == True) and (pwd_match == True) and (format_check == True)):
  print("The passwords matched! Congratulations!!!")
  print(f'{username}, the password you entered was {pwd_hidden} and was {pwd_length} Characters long. Your details have been saved.')
  
elif not(pwd_len == True and pwd_match == True and format_check == False):
    print("Unfortunately the password is in the wrong format, try again. it must be at least 11 characters long, have 1 number, 1 Capital letter, 1 lowercase letter and one symbol'")
  
elif not(pwd_len == True and pwd_match == False and format_check == True):
    print("Passwords did not match, please try again.")
  
elif not(pwd_len == False and pwd_match == True and format_check == True):
    print("Please enter a password with at least 11 characters.")
  
else:
  print("Incorrect password, please input matching passwords with at least 11 characters long, have 1 number, 1 Capital letter, 1 lowercase letter and one symbol")



# password length should be >11
# password should have 1 no
# password should have 1 capital
# password should have 1 lowercase
# password should have 1 symbol
# passwords should match