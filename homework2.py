#number1

# "Given two lists of numbers of the same length, create a new list by multiplying "
# "the pairs of numbers in corresponding positions in the two lists"
# num = [1, 2, 3, 4, 5]
# num2 = [2, 3, 4, 5, 6]
# num3 = []
# for i in range (0, len(num)):
#     num3.append(num[i] * num2[i])
# print((num3))

#number 2 and 3

# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# newList=[]
# for index in range (len(list1)): #number is a variable we just created we are doing len because we are doing two arrays, the word, we need range to show that we are multiplying in the range of the length of the list
    # newNumber = list1[index] * list2[index]
    # newList.append(newNumber) #adding these new numbers to our list
    # print(newNumber)
# print(newList)
#for each item in list 
#make a new number equal to the first positioned items in each list multiplied together 
#add that new number to our new list
#print the new list

#number 2 and 3

# a = [[2,4], [1,6]]
# b = [[4,7], [2,3]]
# new_big_list = []
# # outer
# for indexOne in range(len(a)):
#     # a[index] b[index]
#     # [2,4]       [4,7]
#     new_small_list = []
#     # inner
#     for indexTwo in range(len(a[indexOne])):
#         sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
#         new_small_list.append(sum_of_values)
#     new_big_list.append(new_small_list)
# print(new_big_list)

#4
#Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list
# aList=[1, 2, 2, 3, 4, 4, 8, 0, 9]
# bList=aList.copy()
# bList=list(dict.fromkeys(bList))
# print(bList)


# another more efficient way to do number 4

# original= [1, 2, 2, 3, 1]
# newlist=[]
# for item in original:
#     if item in newlist:               #checking to see if item variable which is going thru newList, and previously went thru original list has any duplicates, if it didnt have any duplicate it'll go to else and and add the item to our new list.
#         print ("You don't need to add "+str(item)+" again.")
#     else:
#         newlist.append(item)
#         print( "Added "+str(item))
# print (newlist)


#5
# string = input('Enter some text: ')

# for char in string:
# 	if char == 'a':
# 		string = string.replace('a','4')
# 	elif char == 'b':
# 		string = string.replace('b','8')
# 	elif char == 'e':
# 		string = string.replace('e','3')
# 	elif char == 'l':
# 		string = string.replace('l','1')
# 	elif char == 'o':
# 		string = string.replace('o','0')
# 	elif char == 's': 
# 		string = string.replace('s','5')
# 	elif char == 't':
# 		string = string.replace('t','7')
# 	else:
# 		pass

print(string)
#6
#6 solution:
# string_to_vowel_check = 'Good'
# last_letter = ''
# new_string = ''
# for letter in string_to_vowel_check:
#     is_vowel = False
#     if letter == last_letter:
#         if letter == 'a' or letter == 'A':
#             is_vowel = True
#         elif letter == 'e' or letter == 'E':
#             is_vowel = True
#         elif letter == 'i' or letter == 'I':
#             is_vowel = True
#         elif letter == 'o' or letter == 'O':
#             is_vowel = True
#         elif letter == 'u' or letter == 'U':
#             is_vowel = True
#     last_letter = letter
#     if is_vowel == True:
#         letter = letter*4
#     new_string+= letter
# print(new_string)



#7 

