class Personality:
  '''
  A personality composition for a villager object that holds their gender and personaltiy personality type
  PS: This is because in animal crossing, a villager's personality is different depending on their gender

  Attributes
  -----------
  gender : str
        The gender of the villager
  personalityType : str
        The specific personality type of the villager
  
  Methods
  ---------
  getPersonality() -> str
        Retrieves the two attributes of personality as a single list unit
  '''
  def __init__(self, gender, personalityType, *args):
    '''
    Constructor to build the personality composition

    Parameters
    -----------
    gender : str
          The gender of the villager
    personalityType : str
          The specific personality type of the villager
    '''
    self.gender = gender
    self.personalityType = personalityType
  
  def __str__(self):
    '''
    Returns all personality attributes

    Returns
    -----------
    All personality attributes

    '''
    return self.gender + ", " + self.personalityType
    
  def setPersonality(self) -> str:
    '''
    Returns the personality attributes as an array

    Returns
    -----------
    The personality attributes in a list

    '''
    person=[self.gender,self.personalityType]
    return person
