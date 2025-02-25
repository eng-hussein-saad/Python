import Main
def insert_New_User(fname,lname,email,password,phone):
  userid=0
  try:
    with open("UsersDB.txt","r") as dbfile:
      list=dbfile.readlines()
      if len(list)>0:
        lastuser=list[len(list)-1]
        userid=int(lastuser[0])+1
      else:
        userid=1
  except:
    userid=1
  userlist=[str(userid),fname,lname,email,password,phone]
  userinfo=":".join(userlist)
  userinfo=userinfo.strip("\n")
  data=f"{userinfo}\n"
  try:
    with open("UsersDB.txt","a") as dbfile:
      dbfile.write(data)
  except:
    with open("UsersDB.txt","w") as dbfile:
      dbfile.write(data)
  print("############\n############\n User Created Successfully\n")
  return Main.main()

def chkValidUser(email,password):
  try:
    with open("UsersDB.txt","r") as dbfile:
      allusers=dbfile.readlines()
      for user in allusers:
        userinfo=user.split(":")
        if userinfo[3]==email and userinfo[4]==password:
          return True
      return False
  except Exception as e:
    print(e)
  