class Person:
  def _init_(iself, name, age):
    self.name = name 
    self.age = age 

  def _str_(self):
    return f"{self.name}({self.age})"
  
  pl = person("John", 36)

  print(pl)
