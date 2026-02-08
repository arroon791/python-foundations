name = "Omar Kotb Abdelhamid Kotb"
print(name.upper())
print(name.lower())
print(len(name))


email = input("write your email: ")
email = email.strip().lower()
print("cleaned email: ", email)

if "@" in email:
    print("Valid email format")
else:
    print("Invalid email format")


name = "Omar"
company = "TeamWhale"
working_hours = 8
resume = f"Hello, my name is {name} and I am working at {company} and I work {working_hours} hours a day"
print(resume)
