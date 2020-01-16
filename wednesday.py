#notes on list
# monday = "vale"
# tuesday = "vale"
# wednesday = "vale"
# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# print(days)
# number = [1, 2, 3, 4, 5]
# print(number[0])
# Len() is to get the length/number of elements in a list
# num_elements = len(number)
# print(num_elements)

#modifying something inside a list, what you do is call the list and in [] denote which element u want to change by using it's index
# number[0] = "monday"
# print(number)
# adding items to a list, first way is append so in parenthesis of append we add what we want added and it will be added to the list
# number.append("4")
# print(number)
# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# todos.append("binge watch a show")

# todos.append("go to sleep")

# print(todos)

# index = 0 #the index will start counting from the first item on the list which is pet the cat

# while index < len(todos): #this is where index becomes linked to the indices of the todos list
    # print(f"{index}: {todos[index]}") #the second index here will show the value on the list corresponding the count of the first index, so when index is on 0 the value on the list is pet the cat
    # index += 1




# combining lists

# a = [1, 2, 3, 4]

# b = [5, 6, 7, 7,]
# print(a)
# print(b)
# print(a+b)

#extend method can add multiple items whereas append adds one item at a time

# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.extend(["binge watch a show", "go to sleep"]) ##use name of the list and add .extend too add multiple items to a list at once
# count = 0
# while count < len(todos):
#     print(f"{count}: {todos[count]}")
#     count += 1

## concatening lists (it makes a new, 3rd list it doesnt change the 2 lists that we are adding)

# list_a = [1, 4, 7, 9]

# list_b = [5, 7, 9]

# print(list_a + list_b)

# print (list_a)

#deleting items 

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
# del todos[0] # Removes the first one
# print(todos)
# del todos[1:3] # Removes items at index 1 upto but not including index 3
# print(todos)

#delete items from a list

#exercise 1 adding items to the list with loops


#step1 for loop problems is to always create the variables

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
# add_items = "placeholder"

# while(len(add_items) > 0):
#     add_items = input("what item do you want to add to your list? ")
#     if len(add_items)>0:
#         todos.append(add_items)
#         print(f' your current list is: ')
#         print(f'{todos}')

#     else:
#         break
#     print("your final to do list is: ")
#     print(todos)

# exercise 1 other way but for some reason it doesnt work
# list_1 = []
# to_add = input("add items to your list ")
# while len(to_add) > 0:
#     list_1.extend([to_add]) #adding user's input to our list 1
    # print(list_1)
    # to_add = input("add items to your list ")
    # print(list_1)

    #list slicing we do this to get specific parts of a list using the list's index upto but not including, it doesnt alter original list it just gives u another shorter version of original list

# numbers = [1, 2, 3, 4, 5]
# new_list = numbers[1:5] #will return everything starting from index 1 all the way to index 5 but not including index 5
# print(new_list)

#insert method

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(3, 6) #will insert 6 in the index 3 position
# print(numbers)

#pop method removes item from end of the list

# poppedvalue = numbers.pop()
# print(poppedvalue)
# print(numbers)

#example 2

# while(len(numbers) > 0): #loop will run as long as the length of numbers value is greater than 0
#     print(numbers.pop())
#     print(numbers)

# print("finished")

#number index

# numbers = ["Muhammad", "ali", "fatima"]

# numbers.index("ali") # returns index value of 4
# result = numbers.index("ali")
# print(result)

#copy method

# myList = [1, 2, 3, 4, 5]
# newList= myList.copy()
# newList[0] = "changed"
# print(myList)
# print(newList)

#multiplying lists
# a = [1, 2]

# print(a*3)

# multidimensional lists aka list inside of a list and how to access contents of the inner list
# myList = [[0, 1], [2, 3]]
# myList[0] [1]
# print(myList)

# x = [[2,6],[6,2],[8,2],[5,12]]
# print(x[2]) (this will print out the inner list which is on the 2nd index position)
# print(x[2][1]) (this will print out the content of the inner list which is in the index 2 position, so the content it printed out was 2 because 2 is in the list which is in the inner postion and 2 is in position 1 of the inner list)


#strings are just like lists, therefore you can get the index of strings also, that means you can loop through a string too

# my_string = "hello world"

# print(my_string[4]) #indexing the character of string so this output will print out O

#if you want to slice this then you do this

# print(my_string[6:])


# LOOPING WITH STRINGS

# How do I loop through the characters of a String?
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = 0
# while index < len(alphabet): 
#     print(alphabet[index]) #as long as the index is less than the length of the string the loop will run
    # index += 1

#converting a string to a list

# print(type(alphabet)) #wanting to know if this is a string or a list and it prints as a string


#convert string to a list 
# alph2 = list(alphabet)
# print(type(alph2)) #now it prints as a list

# converting a list to a string (go over again)

# alphabet1="abcdefghidsk"
# alph_list = list(alphabet1)

# print(type(alph_list))
# alph_str = " ".join(alph_list)
# print(alph_str)


#tuples

# myTuple = (1, 4, 6, "word")

# myTuple[1]
# print(myTuple[1])

#FOR LOOP U=YOU USE IT WHEN YOU KNOW WHEN YOU WILL STOP AS OPPOSED TO WHILE LOOPS IN WHICH YOU DO NOT KNOW WHEN YOU WILL STOP
#for condition in range this is the layout for the FOR LOOP because in for loop we know the range or we can set the range
# alphabet1="abcdefghidsk"
# for character in alphabet1 : 
#     print(character)

    #in class practice create a loop that prints out every other number: 1, 3 , 5, 7, ....1000
    
# for num in range(1,1001,2): #the 2 is there to skip even numbers
    # print(num)

    #inner loops 
# for o_index in (1,4): # 1 is starting point
#     for i_index in (5,10):
#         print(o_index)
#         print(i_index)

#in class exercise 2 create multiplicaton table that has to look like 1x1=1 ,1x2=2 ,1x3=3
# for Outerindex in range(1,11):
#     for innerindex in range (1,11):
#         total = Outerindex * innerindex
#         print(str(Outerindex) + " X " + str(innerindex) + "= " + str(total))