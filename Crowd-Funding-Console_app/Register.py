import re
import Main
import connectDB

regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_valid_mail(email):
  if(re.fullmatch(regexEmail,email)):
    return False
  else:
    return True
  
def check_valid_phone(phone):
  if re.findall("01.{10}",phone):
    return True
  else:
    return False
  
  
def registerPage():
  print("##################\nRegister Page\n 0-Back to Main Menu\n##################")
  fname=input("Enter your first name:")
  if fname=="0":
    return Main.main()
  while len(fname)==0 or (not fname.isalpha()):
    fname=input("Please re-enter valid first name:")
  
  lname=input("Enter your last name:")
  while len(lname)==0 or (not lname.isalpha()):
    lname=input("Please re-enter valid last name:")
    
  email=input("Enter your email:")
  while(check_valid_mail(email)):
    email=input("Please re-enter valid email:")
  
  password=input("Enter your password:")
  while len(password)<8:
    password=input("Your password must be at least 8 characters long\nPlease re-enter your password:")
  
  re_password=input("Re-enter your password:")
  while password!=re_password:
    re_password=input("Password doesn't match\nPlease re-enter your password:")
  
  phone=input("Enter your phone number:")
  while(check_valid_phone(phone)):
    phone=input("Please re-enter valid phone number:")
  
  return connectDB.insert_New_User(fname,lname,email,password,phone)