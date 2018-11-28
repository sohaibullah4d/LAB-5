print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (HOME TASK) ")
print("25-NOV-2018")
print("QUESTION NO:3")

def Term(first_term,difference,nth_term):
    a_n_1 = first_term +((nth_term-1)*difference)
    print(a_n_1)
    ask_user = input("Do you want to continue: ")
    ask_user=ask_user.casefold()
    while ask_user == "yes":
        new_nth_term = eval(input("Enter next n: "))
        a_n_2 = first_term + ((new_nth_term-1)*difference)
        print(a_n_2)
        ask_user = input("Do you want to continue: ")
    else:
        print("END")
    
