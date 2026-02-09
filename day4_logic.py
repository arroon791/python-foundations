age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You are an adult")
else:
    print("Go to your mom young man")


is_verified = True
is_active = True
if is_verified and is_active:
    print("Access granted")
else:
    print("Access denied")


is_admin = False
is_moderator = True
if is_admin or is_moderator:
    print("Access granted")
else:
    print("Access denied")


if is_verified and is_active and age >= 18:
    print("Welcome")
else:
    print("Get out")
