class Person:
    a = 20

p = Person()
print(p.a) ## should print 20
p.a = 0  # set a = 0 but only for object instance, this will not affect class variable a value
print(p.a)  ## print 20, as we change from 0 to 20 for object instance
print(Person.a) ## check if class attribute is changed. nope, it issame as earlier