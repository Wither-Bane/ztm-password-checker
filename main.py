username = input("Hi there! Please enter your username: ") # ask for a username

password = input("Please enter your password: ") #ask for a password

password_length = len(password)
password_stars = '*' * password_length #stars representing each character in pass

print(f'{username}, your password {password_stars} is {password_length} long')