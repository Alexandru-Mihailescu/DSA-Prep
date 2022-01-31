#x = 'abcdefghijklm'
#y = x[::-1]

#print(y)

user_input =input("enter a string: ").upper()

reverse_user_in = user_input.upper()[::-1]

if reverse_user_in == user_input:
    print("This is a palindrome.")

else:
    print("Try again lol")