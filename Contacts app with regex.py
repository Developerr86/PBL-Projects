import re
#from IPython.display import clear_output

def email_val(email): 
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b' 
  if(re.fullmatch(regex, email)):
    return email 
  else: 
    x= input('invalid number enter again: ') 
    return email_val(x)

def check_name(name): 
  regex= r'[a-zA-Z"]+' 
  if(re.fullmatch(regex,name)): 
    return name 
  else: 
    x= input("Invalid name enter again: ") 
    return check_name(x)

def check_no(number): 
  regex= r'[0-9]{10}' 
  if(re.fullmatch(regex,number)): 
    return number
  else: 
    x= input('invalid number enter again: ') 
    return check_no(x)

Contacts=[{},{},{}]

for i in range(3):
  x=input("Enter name ")
  Contacts[i]["name"]=check_name(x)
  y=input("Enter number ")
  Contacts[i]["number"]=check_no(y)
  z=input("Enter email ")
  Contacts[i]["email"]=email_val(z)
  print("\n\n")

def show_contacts(contacts):
    for i in contacts:
      print(i) 

def add_contact(contacts):
    name1=input("Enter name: ")
    check_name(name1)
    for z in contacts:
      if name1 == z["name"]:
        print("this person already exists , try updating")
        return None
    num1=input("Enter number ")
    check_no(num1)
    email=input("Enter email ")
    email_val(email)
    contacts.append({"name":name1,"number":num1,"email":email})
    print(contacts)

def delete_contact(contacts, name):
  try:
    for x in contacts:
      if x["name"]==name:
        contacts.remove(x)
    print(contacts)
  except:
    print("invalid entry")

def update_contact(contacts, name):
    choice=input("Enter what to update: ")
    try:
      info=input("Enter new info: ")
      for x in contacts:  
        if x["name"]==name:
          x[choice]=info
    except:
      print("Invalid choice try again")
      NAME=input("Enter name: ")
      return update_contact(contacts,NAME)
        
def search_contact(contacts, name):
    for x in contacts:  
        if x["name"]==name:
          print(x)
        else:
          print("not found")

def savefile():
  f=open("Contacts.txt","w")
  for x in Contacts:
    f.write(x["name"]+","+x["number"]+","+x["email"]+";")
  f.close()

def getcontacts():
  contacts=[]
  f=open("Contacts.txt","r")
  xq=f.readlines()
  xr=xq[0].split(";")
  for qq in xr:
    try:
      z=qq.split(",")
      contacts.append({"name":z[0],"number":z[1],"email":z[2]})
    except:
      pass
  f.close()
  return contacts

savefile() 
Contacts=getcontacts()


Contacts=[]
Contacts=getcontacts()
while True:
  ch=input("\npress s to show contacts\npress a to add contacts\npress u to update contacts\npress d to delete comtacts\npress c to clear screen\npress q to exit\nchoice:")
  if ch=="s":
    Contacts=getcontacts()
    show_contacts(Contacts)
  elif ch=="a":
    add_contact(Contacts)
  elif ch=="u":
    name2=input("Enter the name to update: ")
    update_contact(Contacts,name2)
  elif ch=="d":
    name2=input("Enter the name to update: ")
    delete_contact(Contacts,name2)
  elif ch=="q":
    break
  #elif ch=="c":
    #clear_output()
  else:
    print("invalid input try again")
  savefile()
  Contacts=getcontacts()

print("End")