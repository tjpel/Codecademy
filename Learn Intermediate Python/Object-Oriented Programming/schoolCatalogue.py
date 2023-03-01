class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents

  def setNumberOfStudents(self, number):
    self.numberOfStudents = number

  def __repr__(self):
    return f'A {self.getLevel()} school named {self.getName()} with {self.getNumberOfStudents()} students'

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    return super().__repr__() + f" with a {self.getPickupPolicy()} pickup policy"

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    return super().__repr__() + f' with the following sports teams: {self.getSportsTeams()}'

ps = PrimarySchool("Peter Hobart", 100, "curbside")
print(ps)
hs = HighSchool("SLPHS", 300, ["Tennis", "Football"])
print(hs)