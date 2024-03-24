#this program is designed to slice out the user name and domain name from an email address
#Step 1: Collect Email Address from the User
#Step 2: Slice out the user name using "@" symbol, the first part is the user name, the second part is the domain name
#step 3: Slice out the domain name using "." symbol

def slicer():
    email = input("Enter Your Email Address: ").strip()

    if email.count("@") == 1 and email.count(".") == 1:
        (username, domain_name) = email.split("@")
        (domain_name, tld) = domain_name.split(".")

        print(f"Your username is {username} \nYour domain name is {domain_name} \nYour top level domain is {tld}" + "/n")
    elif email == "exit":
        quit()
    else:
        print("Invalid Email Address")  

while True:
    slicer()
