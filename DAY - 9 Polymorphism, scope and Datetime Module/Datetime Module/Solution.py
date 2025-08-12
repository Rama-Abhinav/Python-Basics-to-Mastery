from datetime import datetime

user_age = input("Enter Date of Birth (YYYY-MM-DD): ").strip().split("-")
user_age = [int(num) for num in user_age]
userage = datetime(user_age[0],user_age[1],user_age[2])
present = datetime.now()

print(f'''
You are {int(present.year)-int(userage.year)} years old.
You were born on a {userage.strftime("%A")}
''')