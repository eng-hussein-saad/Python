def insert_New_Log(email,data):
  try:
    with open("log.txt","r") as dbfile:
      list=dbfile.readlines()
      if len(list)>0:
        lastlog=list[len(list)-1]
        logid=int(lastlog[0])+1
      else:
        logid=1
  except:
    logid=1
  loglist=[str(logid),email,data]
  loginfo=":".join(loglist)
  loginfo=loginfo.strip("\n")
  data=f"{loginfo}\n"
  try:
    with open("log.txt","a") as dbfile:
      dbfile.write(data)
  except:
    with open("log.txt","w") as dbfile:
      dbfile.write(data)
  return

def get_last_log():
  try:  # if file exist
        # try to open file
        with open("log.txt", "r") as dbfile:
            llist = dbfile.readlines()
            # Check if file is empty or not
            if len(llist) > 0:
                llastlog = llist[len(llist) - 1]
                llastlog = llastlog.strip("\n")
                listLastLog = llastlog.split(":")
                logmail = listLastLog[1]
            else:
                logmail = "error"
            return logmail
  except:
        return "error"