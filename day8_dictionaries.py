ticket = {"title": "withdrawal under process",
          "priority": "high", "status": "open"}
print(ticket)


print(ticket["title"])
print(ticket["status"])


ticket["status"] = "closed"
print(ticket)


print(ticket.get("user"))


tickets = [
    {"title": "Deposit issue", "priority": "high", "status": "open"},
    {"title": "Withdrawal delay", "priority": "medium", "status": "open"},
    {"title": "Verification problem", "priority": "low", "status": "closed"}
]

for ticket in tickets:
    print(ticket["title"], "-", ticket["status"])
