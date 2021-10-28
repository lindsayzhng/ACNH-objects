from villager import Villager

class Resident(Villager):
  '''
  A resident inherited object from the villager object that holds their ID, hobby, catchphrase, saying, and friendship level

  Attributes
  -----------
  villagerID : int
        A numerical value that refers to a specific resident
  hobby : str
        The resident's favourite hobby
  phrase : str
        The resident's catchphrase
  saying : str
        The resident's most popular saying 
  friendship : int
        The friendship value that the user has with the resident (from the range 0-5, 5 being the friendliest)
  
  Methods
  -------
  saySomething() -> str
        Prints the resident's saying and catchphrase in one sentence to the console
  getHobby() -> str
        Prints the resident's favourite hobby to the console
  friendshipStatus() -> int
        Prints whether or not the resident and the user are friends to the console
  incrementFriendship() -> None
        Attempts to increase the friendship level of the user and resident
  deincrementFriendship() -> None
        Attempts to decrease the friendship level of the user and resident

  '''

  resident_count=0

  def __init__(self, name, birthday, species, personality, villagerID, hobby, phrase, saying, friendship=0):
    '''
    Constructor to build a resident object with inheritance from a villager object

    Parameters
    -----------
    villagerID : int
        A numerical value that refers to a specific resident
    hobby : str
        The resident's favourite hobby
    phrase : str
        The resident's catchphrase
    saying : str
        The resident's most popular saying 
    friendship : int, optional
        The inital friendship value that the user has with the resident
        The default friendship value is 0 if none is entered

    '''
    super().__init__(name, birthday, species, personality)
    self.villagerID = str(villagerID)
    self.hobby = hobby
    self.phrase = phrase
    self.saying = saying
    self.friendship = str(friendship)
    
    Resident.resident_count += 1
    print("Welcome {} into our village! We are so glad to have you.".format(self.name))
  
  def __str__(self):
    '''
    Returns all resident attributes

    Returns
    -----------
    All resident attributes

    '''
    return str(super().__str__()) + ", " + str(self.villagerID) + ", " + str(self.hobby) + ", " + str(self.phrase) + ", " + str(self.saying) + ", " + str(self.friendship)

  def saySomething(self) -> str:
    '''
    Returns the resident's most popular saying and catchphrase 

    Returns
    -----------
    The resident's saying and catchphrase

    '''
    return self.name + " has something to say! : " + self.saying.rstrip(self.saying[-1]) + ", " + self.phrase + "!"

  def getHobby(self) -> str:
    '''
    Returns the resident's hobby

    Returns
    -----------
    The villager's hobby

    '''
    return self.hobby
    
  def friendshipStatus(self) -> bool:
    '''
    Returns whether or not the user and resident are friends

    Returns
    -----------
    bool
        True if their friendship value is 3 and above 
        False if their friendship value is below 3
    
    '''
    if(self.friendship>=3):
      return True
    else:
      return False
    
  def incrementFriendship(self) -> None:
    '''
    Increases the friendship value of the resident and user by 1
    
    '''
    if(self.friendship >= 5):
      self.friendship=5
    else:
      self.friendship +=1
  
  def deincrementFriendship(self) -> None:
    '''
    Decreases the friendship value of the resident and user by 1
    
    '''
    if(self.friendship<=0):
      self.friendship=0
    else:
      self.friendship -=1
    
  def __del__(self):
    '''
    Deletes the resident from the island, sends them a farewell message, and removes them from the resident count

    '''
    print("Goodbye, {}! We wish you luck on your next big adventure. This town will miss you.".format(self.name))
    Resident.resident_count-=1