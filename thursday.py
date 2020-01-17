# myVar=1 # created a variable and it's value is 1 and we are storing it in the memory
# myVar=2
# def greeting(): #placing it in memory 
#     print("hello world")

# if (myVar == 1):
#     print('hello')

# greeting() #functions are reusable, also now when we run it this function will run, before it wasnt because we had created not called it


# #slide 7 from wk1 thursday notes

# def print_students():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print_students()


# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print_students()

# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print_students()

#loop in function

# def greeting():
#     print("hello")

# for i in range(10):
#     print (greeting())

    #nested functions (not working)

# def separateRuns(): #not working
#     print('******************')
#     print()   
# def getGroceries():
#     print('milk')
#     print('flour')
#     print('sugar')
#     print('butter')
#     print()
#     print(separateRuns())

#parameters

# def greeting(person): #person is parameter
#     print(f'hello {person}') #this line tells you what will happen with your argument

# greeting("kazim") #kazim is argument


#ADD function

# def add(num1, num2):
#     print(num1, num2)

# add(4, 5) #these take the place of num1, num2 in the print line and adds them 

#RETURN STATEMENT

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# result=add(4, 5) #this is using the add function and within this function are two slots, num1 and num2 and the function adds these two numbers using the sum variable

# print(result) #prints theresult variable and remember the result variable is using the add function  and the add function is adding two numbers together, so when we print out result variable we will get that answer

# ## another example of RETURN STATEMENT 

# def concat_lists(list1, list2):
#     concat = list1 + list2 #this is basically what the function will do to any arguments passed by the user
#     return concat

# the_big_list = concat_lists([1, 4, 6], [7, 9 ,0]) #this is using the concat_lists function to add two lists to gethet

# print(the_big_list)

#calculate the average

# def cal_avg(param1, param2, param3, param4):
#     sum = param1+param2+param3+param4
#     avg = sum/4
#     return(avg) #so information can be sent outside
# result = cal_avg(4, 6, 9, 0)
# print(result)
 
 #change above function to be able to send unlimited amount of numbers into the function the amount of numbers should not matter

# def findavg():
    count= 0
    box= []
    user = ()
    while user != "":
        user= input("Enter your number, when finished press enter.")
        if user =="":
            break
        box.append(int(user))
        count += 1
            
    sum= 0
    for number in box:
        sum += number
        print (sum)
        avg = sum/count
    return avg
print (findavg())




### using tuples with return statements

# def myfunction(num1, num2, num3):

#     return num1*2, num2*3, num3*4 #this is a tuple 

# result = myfunction(4, 7, 9)


## threads

# print("hello")

# def greeting(name):
#     print(f'hello{name}')

# students=["kazim", "furqan" , "rayan", "mom", "dad"]

# for name in students: #so the variable name will become each name within the student variable 
#     greeting(name)

# print("bye")


#LOCAL SCOPE (scope is basically where we can access variables) 

#LOCAL VARIABLES 

TAX_RATE = .09  # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00
def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost
total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
print('Total for first order is', total1)
total2 = calculateCost(12, 15)