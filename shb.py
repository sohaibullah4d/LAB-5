print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (QUIZ)#Done at home")
print("25-NOV-2018")
print("QUESTION NO:1")


def A_NUM(num):
    x = num
    order = len(str(num))
    sum = 0
    while x > 0:
        digit = x % 10
        sum += digit ** order
        x //= 10
    if num == sum:
        print(num,"is an Amstrong number")
    else:
        print(num,"is not an Amstrong number")
        
