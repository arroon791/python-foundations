count = 1
while count <= 5:
    print(count)
    count += 1


age = 17
while age < 18:
    age = int(input("Enter your age: "))
print("age accepted", age)


while True:
    command = input("Enter command: ").lower()
    if command == "quit":
        print("Exiting program")
        break
    print("Command received", command)


while True:
    command = input("Order: ").lower()
    if command == "":
        continue
    if command == "apple":
        print("sorry we cant")
        break
    print("Ordering", command)
