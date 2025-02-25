import Main
import datetime
from HomeMenu import homeMenuPage
from Register import check_valid_mail
from connectDB import chkValidUser
from connectLog import insert_New_Log


def loginPage():
  print("##################\nLogin Page\n 0-Back to Main Menu\n##################")
  email=input("Enter your email:")
  if email=="0":
    return Main.main()
  
  while(check_valid_mail(email)):
    email=input("Please re-enter valid email:")
  
  password=input("Enter your password:")
  while len(password)<8:
    password=input("Your password must be at least 8 characters long\nPlease re-enter your password:")
  
  if(chkValidUser(email,password)):
    dataNow=datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    insert_New_Log(email,dataNow)
    return homeMenuPage()
  else:
    print("Wrong email or password\nPlease try again\n")
    return loginPage()