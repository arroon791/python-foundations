def greet(name):
    print("Hello", name)


greet("Omar")
greet("Programmer")


tickets = ["deposit issue",
           "withdrawal delay",
           "verification required"]


def ticket_printer(ticket_list):
    for ticket in ticket_list:
        print("ticket: ", ticket)


ticket_printer(tickets)


def is_adult(age):
    return age >= 18


age = int(input("Enter your age: "))
if is_adult(age):
    print("Access granted")
else:
    print("Access denied")
