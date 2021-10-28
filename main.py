#-----------------------------------------------------------------------------
# Name:        ACNH Objects - Data Structures Assignment (main.py)
# Purpose:     A utilization of classes, objects, attributes, and methods to create  
#                       an island for animal crossing villagers to inhabit and work in
# References:  This program uses the NumPy/SciPy style of documentation as found
#               				here: https://numpydoc.readthedocs.io/en/latest/format.html with
#               				some minor modifications based on Python 3 function annotations
#               				(the -> notation).
#
# Author:      Lindsay Zhang (699411)
# Created:     15-Oct-2021
# Updated:     27-Oct-2021
#-----------------------------------------------------------------------------

#import of libraries
import json
from random import randint
from urllib.request import urlopen
from villager import Villager
from resident import Resident
from personality import Personality
from specialcharacter import SpecialCharacter
from workdays import Workdays

#url for acnh API to retrieve data of residents
urlbase = "http://acnhapi.com/v1/villagers/"

listOfResidents = []
listOfSpecials = []
listOfLiving = []
listOfCurrentlyWorking = []
village = open('theVillage.txt', 'a')

#to keep track of workers on that day
mon=[]
tue=[]
wed=[]
thur=[]
fri=[]
sat=[]
sun=[]

def makeResident(value):
  '''
  To make a resident object from the ACNH API, put that object in the resident list, and write the data/object information into a txt file

  Parameters
  -----------
  a : int 
      the villager ID that appends to the API link to get the villager JSON file
  
  '''
  
  url=urlbase+str(value)

  response = urlopen(url)

  data_json = json.loads(response.read())
  allnames = data_json['name']
  engname = allnames['name-USen']

  ality=Personality(data_json['gender'], data_json['personality'])

  pillager = Resident(engname, data_json['birthday'], data_json['species'], data_json['id'], str(ality.__str__()), data_json['hobby'], data_json['catch-phrase'], data_json['saying'], '0')

  listOfResidents.append(pillager)

  with open("theVillage.txt", "a") as myfile:
    myfile.write(str(pillager)+"\n")

  print(pillager.saySomething())
  print()

  with open('rawvillagers.txt','a') as f:
    json.dump(data_json, f)
  blanks = open('rawvillagers.txt', 'a')
  blanks.write(2*'\n')

#introduction
print("WELCOME TO ICS4U0 ISLAND!")
print("--------------------------------------------------")
print()
print("Let's introduce your first three residents!")
print()

#have three random villagers move into the island to start off with
for i in range(3):
  value = randint(0,391)
  if value in listOfLiving:
    i=i-1
  else:
    listOfLiving.append(value)
    makeResident(value)

#make user object using input
print("--------------------------------------------------")
print("NOW THAT YOU'VE MET YOUR STARTER RESIDENTS, LET'S GET TO KNOW YOU!")
print()
userName=input("What's your name? : ")
userBirthday=input("What about your birthday? (Please keep it to this format : MM/DD) : ")
userGender = input("Your gender? : ")
userType = input("and FINALLY, your personality! : ")
print("--------------------------------------------------")

ality = Personality(userGender, userType)

theUser=Villager(userName, userBirthday, "Human", str(ality.__str__()))

#add user object to theVillage.txt file
with open("theVillage.txt", "a") as myfile:
  myfile.write(str(theUser)+"\n")

#read from a txt filw and make all special character objects
lines=[]
with open('acnhspecial.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip().split(" : ") for line in lines]

for i in range(21):

  ality = Personality(lines[i][3], lines[i][4])
  
  weekBoolean=[0, 0, 0, 0, 0, 0, 0]
  standard=['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  weekdayList=lines[i][6].split(", ")

  for m in range(len(weekdayList)):
    for n in range(len(standard)):
      if(weekdayList[m]==standard[n]):
        weekBoolean[n]=1
        if(n==0):
          mon.append(lines[i][0])
        elif(n==1):
          tue.append(lines[i][0])
        elif(n==2):
          wed.append(lines[i][0])
        elif(n==3):
          thur.append(lines[i][0])
        elif(n==4):
          fri.append(lines[i][0])
        elif(n==5):
          sat.append(lines[i][0])
        elif(n==6):
          sun.append(lines[i][0])
  
  theWeek=Workdays(weekBoolean[0],weekBoolean[1],weekBoolean[2],weekBoolean[3],weekBoolean[4],weekBoolean[5],weekBoolean[6])

  worker = SpecialCharacter(lines[i][0], lines[i][1], lines[i][2], str(ality.__str__()), lines[i][5], str(theWeek))

  listOfSpecials.append(worker)
  yup = open('WORKER.txt', 'a')
  yup.write(str(worker)+'\n')

print("Let's get to know your village a little better, okay?")
print()

#printing the hobbies the villagers have
print("Your villagers have the following hobbies : "+ str(listOfResidents[0].getHobby()) +", "+ str(listOfResidents[1].getHobby()) +", "+ str(listOfResidents[2].getHobby()))

#getting the workers of an inputted day
day = input("HOLD ON - What day is it again? Was it a Monday or... Can you remind me? : ")
print("Right! Of course it's a "+ day+"! That's what I said...'")

weekdays = {
  "Monday" : mon,
  "Tuesday" : tue,
  "Wednesday" : wed,
  "Thursday" : thur,
  "Friday" : fri,
  "Sunday" : sun,
  "Saturday" : sat,
  }

print()
print("Well, these are the Villagers working today: ")
print(weekdays[str(day)])
print()

#adding a new resident object into the island
newVillager=input("NOW, enter a number between 0-391 :")
print("That's just determined the next resident on your island!")
print()
makeResident(newVillager)

#deleting an old resident object
print("Damn, looks like one of your villagers want to leave the island... ")
listOfResidents[1].__del__()
print("--------------------------------------------------")

#conclusion
print("Well, it has been an eventful day, hasn't it? Maybe it's time to say goodnight.")
print("We have lots to do tomorrow.")
print("BYE! See you in the morning.")