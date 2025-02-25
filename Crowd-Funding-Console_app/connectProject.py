from connectLog import get_last_log
import datetime

def insertNewProj(title, details, total, startDate, endDate):
  try: #if file exist
    with open("ProjectsDB.txt","r") as dbfile:
      list=dbfile.readlines()
      if len(list)>0:
        lastproj=list[len(list)-1]
        projid=int(lastproj[0])+1
      else:
        projid=1
  except:
    projid=1
    
  stringDate=datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
  #convert project info to list
  projlist=[str(projid),title,details,total,startDate,endDate,get_last_log(),stringDate]
  projInfo=":".join(projlist)
  projInfo=projInfo.strip("\n")
  data=f"{projInfo}\n"
  
  try: #if file exist
    with open("ProjectsDB.txt","a") as dbfile:
      dbfile.write(data)
  except:
    with open("ProjectsDB.txt","w") as dbfile:
      dbfile.write(data)
  print("Project created successfully\n")
  return


def searchProject(proj):
  try:
    with open("ProjectsDB.txt","r") as dbfile:
      allprojects=dbfile.readlines()
      resultProjects=[]
      for currentProject in allprojects:
        currentProject=currentProject.strip("\n")
        projectInfo=currentProject.split(":")
        if projectInfo[1]==proj or projectInfo[2]==proj or projectInfo[3]==proj or projectInfo[4]==proj or projectInfo[5]==proj:
          resultProjects.append(currentProject)
      return resultProjects
  except Exception as e:
    print(e)
    
    
def viewAllProjects():
  try:
    with open("ProjectsDB.txt","r") as dbfile:
      allprojects=dbfile.readlines()
      resultProjects=[]
      for currentProject in allprojects:
        currentProject=currentProject.strip("\n")
        resultProjects.append(currentProject)
      return resultProjects
  except Exception as e:
    print(e)

def deleteProject(column,proj):
  column=str(column)
  colNum=0
  match column:
    case "title":
      colNum=1
    case "details":
      colNum=2
    case "total":
      colNum=3
    case "startDate":
      colNum=4
    case "endDate":
      colNum=5
    case "id":
      colNum=0
  
  try:
    resultProjects=[]
    with open("ProjectsDB.txt","r") as dbfile:
      loggedUser=get_last_log()
      allprojects=dbfile.readlines()
      for currentProject in allprojects:
        currentProject=currentProject.strip("\n")
        projectInfo=currentProject.split(":")
        if loggedUser==projectInfo[6]:
          if projectInfo[colNum]!=proj:
            resultProjects.append(currentProject)
        else:
          resultProjects.append(currentProject)
    with open("ProjectsDB.txt","w") as dbwfile:
      for currentResult in resultProjects:
        projInfo=currentResult.strip("\n")
        data=f"{projInfo}\n"
        dbwfile.write(data)
  except Exception as e:
    print(e)
    
    
def editProj(column, id, newData):
  column=str(column)
  colNum=0
  match column:
    case "title":
      colNum=1
    case "details":
      colNum=2
    case "total":
      colNum=3
    case "startDate":
      colNum=4
    case "endDate":
      colNum=5
    case "id":
      colNum=0
  try:
    resultProjects=[]
    with open("ProjectsDB.txt","r") as dbfile:
      loggedUser=get_last_log()
      allprojects=dbfile.readlines()
      for currentProject in allprojects:
        currentProject=currentProject.strip("\n")
        projectInfo=currentProject.split(":")
        if loggedUser==projectInfo[6]:
          if projectInfo[colNum]==id:
            projectInfo[colNum]=newData
            newProjInfo=":".join(projectInfo)
            newProjInfo=newProjInfo.strip("\n")
            currentProject=newProjInfo
          resultProjects.append(currentProject)
    with open("ProjectsDB.txt","w") as dbwfile:
      for currentResult in resultProjects:
        projInfo=currentResult.strip("\n")
        data=f"{projInfo}\n"
        dbwfile.write(data)
  except Exception as e:
    print(e)