# # Given the following Person class:

# class Person: 
#     def __init__(self, name, email, phone):
#       self.name = name #constructor will be defining these instance variables
#       self.email = email #these are called instance variables and are created by the constructor
#       self.phone = phone
#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name)) #other_person is just a placeholder for whatever argument you pass thru this method
# # Write code to

# # number 1 Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# # number 2 Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# # number 3 Have sonny greet jordan using the greet method.
# # number 4 Have jordan greet sonny using the greet method.
# # number 5 Write a print statement to print the contact info (email and phone) of Sonny.
# # number 6 Write another print statement to print the contact info of Jordan.

# #answer to question vvvv

# Sonny= Person ('Sonny', 'sonny@gmail.com', '483-485-4948' ) #Number 1
# Jordan= Person ('Jordan', 'Jordan@gmail.com', "281-713-1800") #Number 2
# Sonny.greet(Jordan)                                         ##Number 3 (when jordan is passed so are all the variables that come along with jordan such as his name email and phone number, and whichever of these variables are used by the greet argument will be shown)
# Jordan.greet(Sonny)                                           #number 4
# print(f'{Sonny.email} {Sonny.phone} {Sonny.name}')              #number 5
# print(f'{Jordan.name}, {Jordan.email}, {Jordan.phone}')         #Number 6