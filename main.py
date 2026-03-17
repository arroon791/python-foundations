import tickets_utils

tickets = []
while True:
    title = input("Enter ticket title (or 'done'): ")
    if title.lower() == "done":
        break
    ticket = tickets_utils.create_ticket(title)
    tickets.append(ticket)
for ticket in tickets:
    tickets_utils.print_ticket(ticket)


tickets_utils.save_tickets(tickets)
