# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Megan during class time


def avg(user_list):
    sumOfNumbers = 0
    for x in user_list:
        sumOfNumbers = sumOfNumbers + x
    avg = sumOfNumbers / len(user_list)
    return avg


if __name__ == '__main__':

    user_list = []
    num = 0
    while num != 'done':
        num = input("Enter a number to be averaged. If you are done, type 'done'. ")
        if num == 'done':
            break
        num = int(num)
        user_list.append(num)


    print("The average of these values is ", avg(user_list))



    # test your fucntion with this print statement before writing the input loop
    
    #print(avg([0, 13, 2]))    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    #user_list = [9,8,2,1,44] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
