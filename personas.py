class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_hello(self):
    print(f'Hello, my name is {self.name} and I am {self.age} years old')


if __name__ == '__main__':
  Miguel = Person('Miguel', 22)

  print(f'Age: {Miguel.age}')
  print(f'Name: {Miguel.name}')
  Miguel.say_hello()