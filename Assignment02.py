# Assignment 02 Resubmit DATA 605 Shreshta Phogat 09/07/2020
List1 = []
while True: 
    try: 
        # limits the range of input to 10 digits
        for i in range (10): 
            # appends the empty list to include only user input integers
            List1.append(int(input('Please enter 10 Integers (0-9) one at a time:')))
        print(List1)
        # Ends list after 10 inputs
        break
        # if any value errors ocurr the user is requested to retry 
    except (ValueError,IOError) as errr:
            print ('Only integers are allowed please retry:')
        # limits user inputs
            if List1 in [1,2,3,4,5,6,7,8,9,0]:
                break

# converting the string of data to floats for easy manipulation
list_of_floats = []
for num in List1:
    list_of_floats.append(float(num))
# Finding the minimum
mini=11
for num in List1:
    if mini>num:
        mini=num
print('minimum : '+str(mini))
# finding the maximum
maxi=0
for num in List1:
    if maxi<num:
        maxi=num
print('maximum :'+str(maxi))
# calculate the range using the max and min calculated previously 
print("Range:", (maxi - mini) )
# Calculate the mean
sums = 0
for num in List1:
    sums += int(num)
    avg= sums/10
    # Show the mean to the user
    print("Mean:", avg)
    # calculate the Varience 
    var1 = sum((i - avg) ** 2 for i in list_of_floats ) / len(list_of_floats) 
    # show the varience to the user
    print("Variance: " + str(var1)) 
    # calculate the standard deviation
    Dev1 = var1 ** 0.5
    # show the user the standard deviation
    print("Standard Deviation: " + str(Dev1)) 
    break