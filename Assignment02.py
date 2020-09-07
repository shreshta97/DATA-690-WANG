# Assignment 02 DATA 605 Shreshta Phogat 09/06/2020

while True:
    # Input function prompts user to enter data 
    Input_Integers = input("Please enter 10 Integers(0-9)separated by a single space only ")
    print("\n")
    # Ensure the Input_Integers can be split by a single space
    Integer_list = Input_Integers.split() 
    # shows user data they inputed
    print("Integer list: ", Integer_list) 
    # converting the string of data to floats for easy manipulation
    list_of_floats = []
    for num in Integer_list:
        list_of_floats.append(float(num))
    # Ensure the user is only able to input numbers
    if Input_Integers.isdigit(): 
        print ("Only integers are allowed please retry 0-9\n")
        # continues the loop
        continue 
    # Ensure the user is only able to input 10 digits    
    elif len(Integer_list) != 10:
        print ("Enter 10 digits\n,")
        # continues the loop
        continue
        
    else: 
            # find the sum of the Integer_list for easy manipulation of statistical data
            sums = 0
            for num in Integer_list:
                sums += int(num)
            # show sum to user
            print("Sum = ", sums)
            # find the smallest digit in the series
            print("Minimum:", * sorted(Integer_list) [:1])
            # find the largest digit in the series
            print("Maximum:", * sorted(Integer_list) [-1])
            # find the difference between the largest and smallest numbers
            print("Range:", [9-0]) 
            # Calculate the mean
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
    break # End the loop