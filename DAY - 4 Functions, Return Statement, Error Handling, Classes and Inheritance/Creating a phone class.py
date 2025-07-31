#🧪 Challenge: Build a Phone Class
    #🎯 Task:
        #Create a class called Phone that has:
            #✅ 1. Constructor (__init__)
                #It should accept and store the following attributes:
                    #brand (e.g., "Samsung", "iPhone")
                    #model (e.g., "Galaxy S23", "13 Pro")
                    #price (as a number)

            #✅ 2. Methods:
                #phone_info() → Print the phone's full info like:
                    # Brand: Samsung
                    # Model: Galaxy S23
                    # Price: ₹70000
                # make_call(number) → Print:                           # Take Number from User
                    # Calling <number> from my <brand> <model>...

            # ✅ 3. Create 2 Phone Objects with different values and:
                # Call phone_info() on both
                # Make a call from one of them

            # 🧠 Example Output:

                # Brand: iPhone
                # Model: 13 Pro
                # Price: ₹120000

                # Calling 9876543210 from my iPhone 13 Pro...

#------------------SOLUTION-----------------------------------#

class Phone:

    def __init__(self, brand, model, price, number):
        self.brand = brand
        self.model = model
        self.price = price
        self.number = number
    
    def phone_info(self):
        print(f'''
              
Brand : {self.brand}
Model : {self.model}
Price : {self.price}

''')

    def make_call(self):
        print(f"Calling {self.number} from my {self.brand} {self.model}...")


phones = []

while True:
    print("\nEnter Phone Details")
    brand = input("Brand: ")
    model = input("Model: ")
    price = input("Price: ")
    number = input("Phone Number: ")

    phone = Phone(brand, model, price, number)
    phones.append(phone)

    more = input("Do you want to add another phone? (yes/no): ").lower()
    if more != 'yes':
        break

# Show all phones
for phone in phones:
    phone.phone_info()
    phone.make_call()


