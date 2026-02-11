capital_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters=capital_letters.lower()
numbers="0123456789"
characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"
print("hi! welcome to the password strength checker")
password=input("enter your password:   ")
length=False
capital_l=False
small_l=False
char=False
num=False
if len(password) >=8:
    length=True
for i in password:
    if i in capital_letters:
        capital_l=True
    if i in small_letters:
        small_l=True
    if i in characters:
        char=True
    if i in numbers:
        num = True

strength=100
if length==False:
    strength-=20
    print("password length should be >= 8 ")
if capital_l==False:
    strength-=20
    print("password should contain CAPITAL LETTERS")
if small_l==False:
    strength-=20
    print("password should contain small letters")
if char==False:
    strength-=20
    print("password should contain atleast one special character")
if not num:
    strength -= 20
    print("password should contain at least one number")

print(f"Your password is {strength}% secure")
