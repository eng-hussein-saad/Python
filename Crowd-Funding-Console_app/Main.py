import Login
import Register
def main():
  print("1-Login\n2-Register\n3-Exit")
  msg1=input("Enter your choice:")
  msg1=int(msg1)
  match msg1:
    case 1:
      return Login.loginPage()
    case 2:
      return Register.registerPage()
    case 3:
      exit()
    case _:
      print("-----------------\nInvalid input\n----------------")
      return main()