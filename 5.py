print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (HOME TASK) ")
print("25-NOV-2018")
print("QUESTION NO:5")

# Marksheet
def std_data(name,F_name,Roll_num):
    print("STUDENT NAME: ",name,"\nSTUDENT'S FATHER NAME: ",F_name,"\nSTUDENT ROLL NUMBER: ",Roll_num)
def sub_detail(sub1,sub2,sub3,sub4,sub5,num1,num2,num3,num4,num5):
        Tmarks=500
        Gmarks=(num1+num2+num3+num4+num5)
        percentage=((Gmarks*100)/Tmarks)
        print(sub1,"=",num1)
        print(sub2,"=",num2)
        print(sub3,"=",num3)
        print(sub4,"=",num4)
        print(sub5,"=",num5)
        print("You have obtained",Gmarks,"marks out of",Tmarks,"marks")
        if (percentage >=80):
           print("Grage = A+")
        elif (percentage<80) and (percentage>=70):
           print("Grade = A")
        elif (percentage<70) and (percentage>=60):
           print("Grade = B")
        elif (percentage<60) and (percentage>=50):
           print("Grade = C")
        elif (percentage<50) and (percentage>=60):
           print("Grade = D")
        elif (percentage<40) and (percentage>=50):
           print("Grade = E")
        else:
           print("Grade = FAIL")
        print("You percentage is",percentage,"%")
