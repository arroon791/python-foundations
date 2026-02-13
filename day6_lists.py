tasks = ["login", "create_ticket", "update_ticket", "close_ticket"]
print(tasks)
print(tasks[0])
print(tasks[3])


tickets = []
tickets.append("deposit")
tickets.append("withdrawal")
tickets.append("verification")
print(tickets)

tickets.pop(1)
print(tickets)


if len(tickets) == 0:
    print("No open tickets")
else:
    print("open tickets: ", len(tickets))


while True:
    title = input("Please enter the ticket title: ").strip()
    if title.lower() == "done":
        break
    tickets.append(title)
print("FInal tickets list: ", tickets)
