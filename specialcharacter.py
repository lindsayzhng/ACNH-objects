from villager import Villager

class SpecialCharacter(Villager):
  '''
  A special character (like the employees of the island) object that inherits from the villager object
    that holds the service they provide and their work days

  Attributes
  -----------
  service : str
        The job that the special character has
  workDay : bool
         The days of the week that the special character works and doesn't work on
  
  Methods
  --------
  getService() -> str
        Prints the job that the special character has to the console
  '''

  def __init__(self, name, birthday, species, personality, service, workDay):
    '''
    Constructor to build a special character object from a villager object

    Parameters
    -----------
    service : str
          The job that the special character has on the island
    workDay : bool
          The days that the special character works and doesn't work
    '''
    super().__init__(name, birthday, species, personality)
    self.service = service
    self.workDay = workDay
  
  def __str__(self):
    '''
    Returns all special character Attributes

    Returns
    -------
    All special character attributes
    '''
    return super().__str__() + ", " + self.service + ", " + self.workDay

  def getService(self) -> str:
    '''
    Returns the special character's job

    Returns
    -------
    The special character's job
    '''
    return self.service
