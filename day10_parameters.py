def create_ticket(title, priority):
    print("Ticket: ", title)
    print("priority: ", priority)


create_ticket("withdrawal", "high")
create_ticket(priority="moderate", title="deposit")


def default_ticket(title, priority="Normal"):
    print("Ticket: ", title)
    print("priority: ", priority)


default_ticket("verification issue")
default_ticket("verification issues", priority="high")
