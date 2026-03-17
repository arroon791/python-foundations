def create_ticket(title):
    return {"title": title, "status": "open"}


def print_ticket(ticket):
    print(ticket["title"], "-", ticket["status"])


def save_tickets(tickets):
    with open("tickets.txt", "w") as file:
        for ticket in tickets:
            file.write(ticket["title"] + "\n")
