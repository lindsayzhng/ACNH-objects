class Workdays:
  '''
  A work day composition for a special character object that determines if they are working on a specific week day
  
  Attributes
  -----------
  mon : bool
        The special character's work availability for Monday
  tue : bool
        The special character's work availability for Tuesday
  wed : bool
        The special character's work availability for Wednesday
  thur : bool
        The special character's work availability for Thursday
  fri : bool
        The special character's work availability for Friday
  sat : bool
        The special character's work availability for Saturday
  sun : bool
        The special character's work availability for Sunday

  Methods
  ---------
  isWorking(work : str) -> bool
        Determines whether or not the special character is working on a string value that denotes the day
  '''
  def __init__(self, mon, tue, wed, thur, fri, sat, sun):
    '''
    Constructor to build a work day composition for a special character object
    
    Parameters
    -----------
    mon : bool
        The special character's work availability for Monday
    tue : bool
        The special character's work availability for Tuesday
    wed : bool
        The special character's work availability for Wednesday
    thur : bool
        The special character's work availability for Thursday
    fri : bool
        The special character's work availability for Friday
    sat : bool
        The special character's work availability for Saturday
    sun : bool
        The special character's work availability for Sunday
    '''
    self.Monday=mon
    self.Tuesday=tue
    self.Wednesday=wed
    self.Thursday=thur
    self.Friday=fri
    self.Saturday=sat
    self.Sunday=sun

  def __str__(self):
    '''
    Returns all attributes of the week day composition

    Returns
    --------
    All attributes of the week day composition

    '''
    return str(self.Monday) + ", " + str(self.Tuesday) + ", " + str(self.Wednesday) + ", " + str(self.Thursday) + ", " + str(self.Friday) + ", " + str(self.Saturday) + ", " + str(self.Sunday)


  def isWorking(self, work : str) -> bool:
    '''
    Returns whether or not the special character will work on a specific day

    Parameters
    ------------
    work : str
            The week day that checks if the special character is working on
    
    Returns
    --------
    bool
          True if the special character is working
          False if the special character is not working
    '''
    if(self.mon==True and work=="Monday"):
      return True
    elif(self.tue==True and work=="Tuesday"):
      return True
    elif(self.wed==True and work=="Wednesday"):
      return True
    elif(self.thur==True and work=="Thursday"):
      return True
    elif(self.fri==True and work=="Friday"):
      return True
    elif(self.sat==True and work=="Saturday"):
      return True
    elif(self.sun==True and work=="Sunday"):
      return True
    else:
      return False