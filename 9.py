print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (HOME TASK) ")
print("25-NOV-2018")
print("QUESTION NO:9")

def encryption(realText,step):
    outText = []
    cryptText = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step)%26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step)%26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
        else:
            outText.append(" ")
    encrypted_text = ''.join(outText)
    return encrypted_text

user_text = input("Please enter a message to encrypt it: ")
text_step = int(input("Please enter a number to encrypt the message with : "))
print(encryption(user_text,text_step))

    
    
