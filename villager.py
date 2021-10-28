#animal crossing villagers
from abc import ABC, abstractmethod

class Villager():
  '''
  A villager object that holds their name, birthday, species, and personality

  Attributes
  -----------
  name : str 
        The name of the Villager
  birthday : str
        The birthday of the villager (example format MM/DD)
  species : str
        The animal species the villager is
  personality : str
        The personality of the villager, characterized by their gender and personality type

  Methods
  -----------
  getName() -> str
	    Prints the name of the villager to the console
  getBirthday() -> str
	    Prints the birthday of the villager to the console
  isBirthday() -> bool
	    Prints if the date entered is the birthday of the villager to the console
  getSpecies() -> str
	    Prints the species of the villager to the console
  getPersonality() -> str
	    Prints the personality of the villager to the console

  '''

  def __init__(self, name, birthday, species, personality):
    '''
    Constructor to build a villager object

    Parameters
    -----------
    name : str 
          The name of the Villager in the town/on the island
    birthday : str
          The birthday of the villager (example format MM/DD)
    species : str
          The animal species the villager is
    personality : str
          The personality of the villager, characterized by their gender and personality type

    '''
    self.name = name
    self.birthday = birthday
    self.species = species
    self.personality = personality
    super().__init__()
  
  def __str__(self):
    '''
    Returns all villager attributes

    Returns
    -----------
    All villager attributes

    '''
    return str(self.name) + ", " + str(self.birthday) + ", " + str(self.species) + ", " + str(self.personality)
  
  def getName(self) -> str:
    '''
    Returns the villager's name

    Returns
    -----------
    The villager's name
    
    '''
    return self.name
  
  def getBirthday(self) -> str:
    '''
    Returns the villager's birthday

    Returns
    -----------
    The villager's birthday
    
    '''
    return self.birthday
  
  def isBirthday(self, date : str) -> bool:
    '''
    Returns whether or not it is the villager's birthday

    Returns
    -----------
    bool
        True if it is the villager's birthday
        False if it is not the villager's birthday
    
    '''
    if(self.birthday == date):
      return True
    else:
      return False
    
  def getSpecies(self) -> str:
    '''
    Returns the villager's species

    Returns
    -----------
    The villager's species
    
    '''
    return self.species
  
  def getPersonality(self):
    '''
    Returns the villager's personality

    Returns
    -----------
    The villager's personality
    
    '''
    return self.personality
  

@abstractmethod
def saySomething(self):
  return

def getHobby(self):
  return
  
def incrementFriendship(self):
  return

def deincrementFriendship(self):
  return

def friendshipStatus(self):
  return

def setPersonality(self):
  return

def getService(self):
  return

def isWorking(self, work : str):
  return
