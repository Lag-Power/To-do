password = input('Enter password')
if len(password) > 7:
    print("Great Password there!")
elif len(password) == 7:
    print("Your password is OK")
else:
    print("Your password is weak!")
