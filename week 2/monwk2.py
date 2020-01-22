# class Greeting:
#     def say_hello(self): #i cant just use the say_hello method anymore cause it is now inside of a class , self is a pointer 
#         print("hello")

# newGreetingObj = Greeting() #we are creating a object when we do this

# newGreetingObj.say_hello() 

# class Student:
#     def morning(self): #method within a class
#         print("good morning")

# sean = Student() #creating a object (we have to create a object within the class to be able to use the method that is inside the class, class is just the template of what we do and how we use the object)
# sean.morning()

# alina = Student() #second object
# alina.morning()

# alex = Student() # third object 
# alex.morning()

#####

#constructor method

# class Student:
#     def __init__(self):
#         print('constructor called')

#     def morning(self): #method within a class
#         print("good morning")

###

#self

#example 1

# class Animal:
#   def __init__ (self, name):                                    #whenevr you create a object based on the animal class it'll call this constructor whereas if u create a object in the dog method it wont be able to call a constructor because there is no constructor method within the dog method
#     self.name = name

# dog = Animal('dog') 

# cat = Animal('cat')

# horse = Animal('horse')


# print(dog.name)
# print(cat.name)
# print(horse.name)


#example 2

# class Student:
#     def __init__(self, name, lname):
#         self.name = name # name is the parameter being passed in, self.name is referring back to the variable which is alina in our case 
#         self.lname = lname #this will find lname within our alina object
#         print(f'{self.name} {self.lname}')

# alina = Student('Alina', 'belova') #this info is going into our constructor, alina is our object

# sean = Student('sean', 'page')

# print(alina.name)




#example 3 using lists

# import datetime

# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname #self is referring to sammy the variable and is making objects (instantializing objects for this variable)
#         self.lname=lname
#         self.birthdate=birthdate
#         self.address=address
#         self.email=email
#     def age(self):  #we making this function/method to calculate sammy's age
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year #here we are calculating sammy's age
        
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age-=1
#         return age


# sammy = Person("Sammy", "Kry", datetime.date(1998, 8, 21), "123 sesame street", "sammy@gmail.com") #by doing sammy=Person sammy's info is now linked to the person class and the objects the person class has such as fname, lname, etc

# print(f"{sammy.fname} {sammy.lname}")

# age=sammy.age()
# print(age)


####
#difference between a function and a class

# def greeting(name):
#     count=0
#     print(f'hello {name}')
#     count+= 1
#     Print(count)
# greeting("daniela")

# greeting("alex")

# greeting("john")

# greeting("meryem")

# class Person:
#     def __init__(self):
#         self.name=self

#     def greeting(self):
#         print(f'hello {self.name}')
#         self.count+=1

#     def printCount(self):
#         print(self.count)

# alina = Person("alina")

# alina.greeting()
# alina.printCount()
# alina.greeting()
# alina.greeting()


######

#ACCESSOR MODIFIERS

#Access modifiers are keywords used to specify the declared accessibility of a member or a type. -public, private, protected, internal

#a method that is started with a underscore is technically considered a private method

# class Person:
#   def __init__ (self, name):
#     self.name = name
#     self.count = 0
#   def greet (self):
#     self._greet()
#   def _greet (self):
#     self.count += 1
#     if self.count > 1:
#       print("Stop being so nice")
#       self.__reset_count()
#     else:
#       print("Hello", self.name)
#   def __reset_count(self):
#     self.count = 0

# Alex = Person("alex") #passing this type the name Alex

# Alex.greet()
# Alex.greet() #since we called greet again it will now print out the if statement "stop being so nice and then it'll reset the count"



####


#INHERITANCE

# class Animal:
#   def __init__ (self, name):
#     self.name = name
# class Dog (Animal):                     #dog class is inheriting the animal class
#   def woof (self):
#     print("Woof")
# class Cat (Animal):
#   def meow (self):
#     print("Meow")



#example 2  print word in reverse

# class VString(str):
#hello
#olleh
#     def reverse(self, name):            #inside of this method that we are making we want this method to reverse the string
        
#         reversedstring = ""

#         for char in name:
#             reversedstring = char + reversedstring
        
#         return reversedstring

# myString=VString("hello")

# print(myString.capitalize())

# reversed = myString.reverse("hello")
# print(reversed)

#example 3 for inheritance (implicit method)

# class Parent():

#     def implicit(self):
#         print("parent implicit()")
# class Child(Parent):
#     pass
# dad=Parent()
# dad.implicit()

# son = Child()
# son.implicit #first son.implicit will look in the child class for implicit, but since i isnt there it'll inherit it from parent class

### inheritance example 4 Override method

# class Parent(object):
#         def override(self):
#             print("PARENT override()")
    
# class Child(Parent):
#         def override(self):
#             print("CHILD override()")
    
#     dad = Parent()
#     son = Child() #son is now linked to the child class and can only get stuff from child class unless when it comes to inheritance
#     dad.override() #calling a specific function within the parent class
#     son.override()



    #### inheritance example 4 super (super is used when we have two methods one method in parent class and the other in child class we use super to be able to use the method in the parent class and not the child class) i can also call other methods within the parent class even if they dont exist in child class


# class Character:
#     def __init__(self, name, power, health):
#         self.name=name
#         self.power=power
#         self.health=health

# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon 
#         super(Hero, self).__init__(name, power, health)

# alina = Hero("pink gun", "alina", 3, 10)

# print(alina.name) #now we have initialized name in the hERO CLASS BY CALLING THE SUPER WITH WHICH WE WERE ABLE TO USE THE PARENT CLASS' INIT METHOD AND WE DIDNT HAVE THE INITALIZED VARIABLES IN THE CHILD FUNCTION SO WE WERE ABLE TO USE THE PARENT FUNCTION'S VARIABLE


######

#PROJECT FOR OBJECT ORIENTED PYTHON

#Number 1

# Make your own class
# Create a class Vehicle. A Vehicle object will have 3 attributes:

# make
# model
# year
# A vehicle is created thus:

# car = Vehicle('Nissan', 'Leaf', 2015)
# And you can access it's attributes individually like so:


# class vehicle:
#     def __init__(self, model, year, make):
#         self.model=model
#         self.year=year
#         self.make=make
#     def print_info(self):
#             vehicle_info = ("Here is the model of the car " f'{self.model} ' "and your car was made on the year " f'{self.year}' "also the make of your car is " f'{self.make}')
#             print(vehicle_info)


# car = vehicle("mercedes", "c300", 2020)
# car.print_info()




#Number2

#Go back to the Person class. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person.

#answer to number 2 v

# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name #constructor will be defining these instance variables
#         self.email = email #these are called instance variables and are created by the constructor
#         self.phone = phone
#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name)) #other_person is just a placeholder for whatever argument you pass thru this method
#     def print_contact_info(self):
#         contact_info = ("here is the name " f'{self.name}' "the email " f'{self.email}' "and the phone number " f'{self.name}')
#         print(contact_info)



# Sonny= Person ('Sonny', 'sonny@gmail.com', '483-485-4948' ) #Number 1
# # Jordan= Person ('Jordan', 'Jordan@gmail.com', "281-713-1800") #Number 2
# # Sonny.greet(Jordan)                                         ##Number 3 (when jordan is passed so are all the variables that come along with jordan such as his name email and phone number, and whichever of these variables are used by the greet argument will be shown)
# # Jordan.greet(Sonny)                                           #number 4
# # print(f'{Sonny.email} {Sonny.phone} {Sonny.name}')              #number 5
# # print(f'{Jordan.name}, {Jordan.email}, {Jordan.phone}')         #Number 6

# Sonny.print_contact_info()


#nUMBER 3
# Add an instance variable (attribute)

# Add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor __init__. Once you've done this you should be able to add a friend to a person using list's append method:

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# You should also be able to get the number of friends a person has by using the len function on his friends:

# >>> len(jordan.friends) 1

# class Person: 
#     def __init__(self, name, email, phone,):
#         self.name = name #constructor will be defining these instance variables
#         self.email = email #these are called instance variables and are created by the constructor
#         self.phone = phone
#         self.friends =[]
#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name)) #other_person is just a placeholder for whatever argument you pass thru this method
#     def print_contact_info(self):
#         contact_info = ("here is the name " f'{self.name}' "the email " f'{self.email}' "and the phone number " f'{self.name}')
#         print(contact_info)

# # Sonny= Person ('Sonny', 'sonny@gmail.com', '483-485-4948' )                            #Number 1
# # Jordan= Person ('Jordan', 'Jordan@gmail.com', "281-713-1800")                                   #Number 2
# # Sonny.greet(Jordan)                                                                                 ##Number 3 (when jordan is passed so are all the variables that come along with jordan such as his name email and phone number, and whichever of these variables are used by the greet argument will be shown)
# # Jordan.greet(Sonny)                                                                                 #number 4
# # print(f'{Sonny.email} {Sonny.phone} {Sonny.name}')                                                  #number 5
# # print(f'{Jordan.name}, {Jordan.email}, {Jordan.phone}')                                                 #Number 6
# Jordan.friends.append(Sonny)
# Sonny.friends.append(Jordan)
# len(Jordan.friends)
# len(Sonny.friends)
# print(Sonny.friends) #prints reference to the list
