print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (HOME TASK) ")
print("25-NOV-2018")
print("QUESTION NO:4")

# function to check if a string is palindrome or not

def string(my_str):
    my_str = my_str.casefold()
    rev_str = reversed(my_str)  #Reverse the string

    #Check if the string is equal to its reverse
    if list(my_str) == list(rev_str):
        print("It is a Palindrome")
    else:
        print("It is not Palindrome")
