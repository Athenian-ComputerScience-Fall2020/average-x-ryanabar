# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#

def avg(user_list):
    sumOfNumbers = 0
    for x in user_list:
        sumOfNumbers = sumOfNumbers + x          
    avg = sumOfNumbers / len(user_list)
    return avg

user_list = [9,8,2,1,44]
print("The average is", avg(user_list))


#if __name__ == '__main__':

    # test your fucntion with this print statement before writing the input loop
    
    #print(avg([0, 13, 2]))    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    #user_list = [9,8,2,1,44] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
