
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def string_to_list(word1):
    l1=[]
    for i in word1:
        l1.append(i)
    return l1




def list_to_string(l):
    s=""
    for i in l:
        s+=i
    return s



def encode(word1,shift_number,alphabets):
    # length_word=len(word)
    word2=string_to_list(word1)
    for i in range(len(word2)):
        if word2[i] in alphabets:
            index_of_I=alphabets.index(word2[i])
            # print(index_of_I)
            word2[i]=alphabets[(index_of_I+shift_number)%26]
    encode_number=list_to_string(word2)
    print("Here is your encoded result:",encode_number) 





def decode(word1,shift_number,alphabets):
    word2=string_to_list(word1)
    for i in range(len(word2)):
        if word2[i] in alphabets:
            index_of_I=alphabets.index(word2[i])
            new_shift_number= shift_number%26
            word2[i]=alphabets[index_of_I-new_shift_number]
    decode_value=list_to_string(word2)
    print("Here is your decoded result:",decode_value)





while True:
# ask user for decode or encode
    print('type "encode" to encrypt, type "decode" to decrypt: ')
    encode_or_decode=input()
#ask user for enter his massage
    print("Enter your massage: ")
    word=input()
    word1=word.lower() # this is converting the word in lower case
#how many word to shift
    print("type the shift nubmer: ")
    shift_number=int(input())

    if encode_or_decode=="encode":
        encode(word1,shift_number,alphabets)
    elif encode_or_decode=="decode":
        decode(word1,shift_number,alphabets)
    else:
        print("Cheak your spelling.....!! Invalid result")


    print("type 'yes' if you want to continue, otherwise 'no'")
    ch=input()

    if(ch=="yes"):
        continue
    elif (ch=="no"):
        print("bye🖐🖐🖐🖐")
        break
    else:
        print("sorry.....!! Invalid choice.")