#Instead of creating classes with empty or default values, we can set these values when we create the instance. 
#This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. 
#To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined.

>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor

>>> jonagold = Apple("red", "sweet")
>>> print(jonagold.color)
Red


>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...

>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet
