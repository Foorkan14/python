# # SMALL QUESTIONS

# # NUMBER 1

# 1. Madlib function
# Write a function that accepts two arguments: a name and a subject.

# The function should return a String with the name and subject interpolated in.

# For example:

# madlib("Jenn", "science")
# # "Jenn's favorite subject is science."

# madlib("Jeff", "history")
# # "Jeff's favorite subject is history."
# Provide default arguments in case one or both are omitted.

# #answer of NUMBER 1 below


# def madlib(person_name , subject_name):
#     print(f'{person_name} favorite subject is {subject_name}')
# sentence = madlib("john" , "science")


#number 2

# Celsius to Fahrenheit conversion
# The formula to convert a temperature from Celsius to Fahrenheit is:

# F = (C * 9/5) + 32

# Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value.

### answwer to number 2 is below v (my version for some reason didnt work so ask teacher )

# def temp_convertor(fahr, cels):
#     conversion = (cels*4/5) + 32
#     fahrenheit = conversion
#     return (fahrenheit) 
#     print (f' the temperature in fahrenheit is {fahrenheit}')
# what_is_temp = temp_convertor(5,20)

# # number 2 answer from alex v

# def CtF():
#     C = int(input("Place the temperature here, in C "))
#     return (C * 9/5) + 32

# number 4
# Write a function that accepts a number as an argument and returns a Boolean value. Return True if the number is even; return False if it is not even

#answer to number 4 is below v

# def is_even (number):
#     if (number % 2) == 0:
#         return(True)
#     else:
#         return(False)

# the_number = is_even(5)
# print(the_number) 

#medium questions

# NUMBER 1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

# answer to number 1

# def smallest_Number(my_List):
#     return min(my_List)
# aList = [1, 2, 3]
# myList = smallest_Number(aList)
# print(myList)

#answer to number 2
# bigList = [3, 9, 8, 10]
# def largest_Number(big_boy_list):
#     return max(big_boy_list)
# print(largest_Number(bigList))

#number 3

# Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List
# list[]
# def aString(listofStrings)
#     for letters in list


#NUMBER 4 (REVIEW IT GO OVER IT)
# Find the longest String
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:#HERE n is the variable and it will be taking the form of any variable that goes inside the function
        word_len.append((len(n), n)) #now we will be checking the length of each word on the list  
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))