# exampleList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# for eachNumber in exampleList:
#     print(eachNumber)
 ###
 #days and weeks nested for loop practice

weeks = [1, 2, 3, 4, 5]
days = ["mon", "tues", "wed", "thurs", "fri"]
subjects = ["lecture , hwk , solutions"]
for outer_var in weeks: #outer var will loop for every number in the weeks variable
    print(f'week {outer_var}')
    for inner_variable in days:     ## nner_variable becomes the days of the week one by one because those days represent how many times inner for loop will run. and when it arrives on friday the outer loop will then run
        print(f' {inner_variable}')
        for subject in subjects:    #now subject will become lecture,hwk,solutions and as soon as it complets its's loop the loop before it will start and so on and so forth
            print(f'{subject}')
    