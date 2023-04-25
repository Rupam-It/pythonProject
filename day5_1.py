# this a project for ramndom password generator
import random
print("Welcome to Rupam's password generator...!!!")
int_num=['0','1','2','3','4','5','6','7','8','9'] # only number are uswually used in password

# num=str(int_num)

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
# this letters are used for password

symbols=['!','@','$','%','^','&','*','(',')','_','-','+','[',']','{','}',';','?','.',',','<','>']

print("How many letter would you like in your password?")
total_letters=int(input())

print("How many numbers would you like?")
total_numbers=int(input())

print("How many symbols would you like?")
total_symbols=int(input())


# number of letters is rest of number and symbols
no_letters=total_letters-total_numbers-total_symbols
password="" # this is an empty password

# we adding leters to the password
for i in range(0,no_letters):
    l=random.choice(letters)
    # print(l)
    password+=l

# adding numbers to password
for i in range(0,total_numbers):
    n=random.choice(int_num)
    # print(n)
    password+=n

# adding symbols to the letters
for i in range(0,total_symbols):
    s=random.choice(symbols)
    # print(s)
    password+=s

# converting a string to list for shuffle
pw=[]
for p in password:
    pw.append(p)

#shuffle the list 
random.shuffle(pw)
password=""

#converting list p to a string
for char in pw:
    password+=char


print("\n\nHere is your password:",password)