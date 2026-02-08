name = "Omar Kotb Abdelhamid"
age = 23

learning_programming_seriously = True
learning_programming_for_fun = False

dedicated_hours = 2.5

print("My name is", name)
print("I am", age, "years old")
print("Am I learning programming for fun? ", learning_programming_for_fun)
print("Am I learning programming seriously? ", learning_programming_seriously)
print("I dedicate", dedicated_hours, "hours every day")


user_age = input("Enter your age: ")
user_age = int(user_age)
next_year_age = user_age + 1
print("Next year you will be", next_year_age)


age = int(input("Enter your age: "))
if age >= 18:
    print("access granted")
else:
    print("access denied")
