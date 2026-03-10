while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break
    except ValueError:
        print("Please enter a valid age bitch!")

print("Age accepted:", age)


tickets = []
while True:
    title = input("Enter ticket title (or 'done'): ")
    if title.lower() == "done":
        break
    tickets.append({"title": title, "status": "open"})
    if not title.strip():
        print("title can not be empty.")
        continue
print(tickets)
