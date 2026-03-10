ticket = {
    "title": "Deposit issue",
    "priority": "High",
    "status": "Open"
}

for key in ticket:
    print(key, ":", ticket[key])


for key, value in ticket.items():
    print(key, ":", value)


tickets = [
    {"title": "Deposit issue", "priority": "High"},
    {"title": "Withdrawal delay", "priority": "Medium"},
    {"title": "Verification problem", "priority": "Low"}
]


for ticket in tickets:
    print(ticket["title"], "-", ticket["priority"])


coordinates = (10, 20)
x, y = coordinates

print("x: ", x)
print("y: ", y)
