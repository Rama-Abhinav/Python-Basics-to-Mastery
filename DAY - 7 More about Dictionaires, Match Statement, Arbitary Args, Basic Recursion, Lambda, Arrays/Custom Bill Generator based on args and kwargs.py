"""
🧪 Problem: Custom Bill Generator
    📝 Task:
        Write a function generate_bill(*items, **details) that:

        > Accepts any number of item prices as *args.

        > Accepts customer details like name, email, etc. as **kwargs.

        > Prints the total amount and shows the customer details neatly.

        ✅ Example Call:

            generate_bill(100, 250, 50, name="Alice", email="alice@example.com", location="Delhi")

        🎯 Expected Output:
            
            Customer Details:
            Name: Alice
            Email: alice@example.com
            Location: Delhi

            Total Items: 3
            Total Bill: ₹400
"""

def generate_bill(*items, **details):
    print(f"\nCustomer Details:\nName:{details["Name"]}\nEmail:{details["Email"]}\nLocation:{details["Location"]}\n\nTotal Items:{len(items)}\nTotal Amount: {sum(items)}")


Cost_Items = input("Enter The Price Of Each Item Purchased (seperated by commas {,} ): ").split(",")
Cost_Items = tuple([int(x) for x in Cost_Items])
Name = str(input("Enter Your Name: "))
Email = str(input("Enter Your Email (YourEmail@gmail.com): "))
Location = str(input("Enter The Location In which you live (like Delhi, Bengaluru, etc.): "))

generate_bill(*Cost_Items, Name = Name, Email = Email, Location = Location)  ## Add the * before the *arg,*items to treat it as an arbitary postional argument.
