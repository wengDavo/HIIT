# This program takes in an input
# i print the first 2 characters using index slicing
# i print the last 2 characters using index slicing
# i print the middle elements by calculating the length
# of the string and dividing by 2
# and then slice the list from the middle


def work_5():
    msg = "Ënzo Fernandez"
    print("First 2:", msg[0:2])
    print("Last 2:", msg[-2:])
    mid = len(msg)//2
    print("Middle Elements:", msg[mid:mid+2])


work_5()
