tickets = ["withdrawal processed",
           "verification required", "deposit not appear"]
with open("tickets.txt", "w") as file:
    for ticket in tickets:
        file.write(ticket + "\n")

print("Tickets saved")


with open("tickets.txt", "r") as file:
    for line in file:
        print(line.strip())


new_ticket = input("Enter a new ticket: ")
with open("tickets.txt", "a") as file:
    file.write(new_ticket + "\n")
print("Ticket added")
