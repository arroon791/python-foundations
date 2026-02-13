tickets = ["deposit issue", "withdrawal delay", "verification timeframe"]
for ticket in tickets:
    if "deposit issue" in ticket:
        print("High priority", ticket)
    else:
        print("Normal priority", ticket)
print("Total tickets: ", len(tickets))


for number in range(1, 6):
    print(number)


for i in range(3):
    for j in range(2):
        print("i: ", i, "j: ", j)
    break
