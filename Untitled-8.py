class person:
  def _init_(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("HeLLo my name is " + self.name)

pl = person("John", 36)
pl.myfunc()