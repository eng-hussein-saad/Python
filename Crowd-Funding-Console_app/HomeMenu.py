import Main
import connectProject

def homeMenuPage():
  print("##################\nHome Menu\n 0-Back to Main Menu\n##################")
  print(
        "\t1-View All Projects\n\t2-Insert New Project\n\t3-Edit Project\n\t4-Delete Project\n\t"
        "5-Search In Projects\n\t0-To back main menu")
  menuNum=input("Enter your choice:")
  if menuNum=="0":
    return Main.main()
  
  match menuNum:
    case "1":#all projects
      print(connectProject.viewAllProjects())
    case "2":#Insert new project
      InsertProjectPage()
    case "3":#edit projecct
      chooseColumn("edit")
    case "4":#delete project
      chooseColumn("delete")
    case "5":#search in projects
      projSearch=input("0-Back to Home Menu\nEnter your search:")
      if projSearch=="0":
        return homeMenuPage()
      while len(projSearch)==0:
        projSearch=input("Please re-enter valid search:")
      print(connectProject.searchInProjects(projSearch))
    case 0: #back to main menu
      return Main.main()
    case _:
      print("-----------------\nInvalid input\n----------------")
      return homeMenuPage()
  return homeMenuPage()


def chooseColumn(operation):
   print("\t1-Title\n\t2-Details\n\t3-Total\n\t4-Start Date\n\t5-End Date\n\t6-Project ID\n\t0-To back main menu")
   column = input("############################\nEnter Number of your choice: ")
   if column == "0":
     return homeMenuPage()
   
   column = int(column)
   
   match column:
     case 1: #title
       if operation == "edit":
         data=input("Enter old title data:")
         while len(data)==0:
           data=input("Please re-enter valid old title data:")
          
         newData=input("Enter new title data:")
         while len(newData)==0:
           newData=input("Please re-enter valid new title data:")
           
         connectProject.editProj("title",data,newData)
       else:
        data=input("Enter title data:")
        while len(data)==0:
          data=input("Please re-enter valid title data:")
        connectProject.deleteProject("title",data)
     case 2: #details
       if operation == "edit":
         data=input("Enter old details data:")
         while len(data)==0:
           data=input("Please re-enter valid old details data:")
          
         newData=input("Enter new details data:")
         while len(newData)==0:
           newData=input("Please re-enter valid new details data:")
           
         connectProject.editProj("details",data,newData)
       else:
        data=input("Enter details data:")
        while len(data)==0:
          data=input("Please re-enter valid details data:")
        connectProject.deleteProject("details",data)
     case 3: #total
       if operation == "edit":
         data=input("Enter old total data:")
         while len(data)==0:
           data=input("Please re-enter valid old total data:")
          
         newData=input("Enter new total data:")
         while len(newData)==0:
           newData=input("Please re-enter valid new total data:")
           
         connectProject.editProj("total",data,newData)
       else:
        data=input("Enter total data:")
        while len(data)==0:
          data=input("Please re-enter valid total data:")
        connectProject.deleteProject("total",data)
     case 4: #startDate
       if operation == "edit":
         data=input("Enter old startDate data:")
         while len(data)==0:
           data=input("Please re-enter valid old startDate data:")
          
         newData=input("Enter new startDate data:")
         while len(newData)==0:
           newData=input("Please re-enter valid new startDate data:")
           
         connectProject.editProj("startDate",data,newData)
       else:
        data=input("Enter startDate data:")
        while len(data)==0:
          data=input("Please re-enter valid startDate data:")
        connectProject.deleteProject("startDate",data)
     case 5: #endDate
       if operation == "edit":
         data=input("Enter old endDate data:")
         while len(data)==0:
           data=input("Please re-enter valid old endDate data:")
          
         newData=input("Enter new endDate data:")
         while len(newData)==0:
           newData=input("Please re-enter valid new endDate data:")
           
         connectProject.editProj("endDate",data,newData)
       else:
        data=input("Enter endDate data:")
        while len(data)==0:
          data=input("Please re-enter valid endDate data:")
        connectProject.deleteProject("endDate",data)
     case 6: #id
       if operation == "edit":
         data=input("Enter old id data:")
         while len(data)==0:
           data=input("Please re-enter valid old id data:")
          
         newData=input("Enter new id data:")
         while len(newData)==0:
           newData=input("Please re-enter valid new id data:")
           
         connectProject.editProj("id",data,newData)
       else:
        data=input("Enter id data:")
        while len(data)==0: 
          data=input("Please re-enter valid id data:")
        connectProject.deleteProject("id",data)
     case 0: #back to main menu
       return Main.main()
     case _:
       print("-----------------\nInvalid input\n----------------")
       return homeMenuPage()
     

def InsertProjectPage():
  print("############################\nWelcome to Project Info Page\n0-To back main "
          "menu\n############################")
  projTitle=input("Enter project title:")
  if projTitle == "0":
    return homeMenuPage()
  while len(projTitle)==0:
    projTitle=input("Please re-enter valid project title:")
  
  projDetails=input("Enter project details:")
  while len(projDetails)==0:
    projDetails=input("Please re-enter valid project details:")
  
  projTotal=input("Enter project total:")
  while not projTotal.isdigit():
    projTotal=input("Please re-enter valid project total:")
  
  projStartDate=input("Enter project start date:")
  while len(projStartDate)!=10:#yyyy-mm-dd
    projStartDate=input("Please re-enter valid project start date:")
  
  projEndDate=input("Enter project end date:")
  while len(projEndDate)!=10:#yyyy-mm-dd
    projEndDate=input("Please re-enter valid project end date:")
  
  connectProject.insertNewProj(projTitle,projDetails,projTotal,projStartDate,projEndDate)
  print("Project inserted successfully\n")
  return homeMenuPage()