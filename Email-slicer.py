#    Email-slicer   ##

email=input("Enter your Email: ")
s=" "
if s not in email:
    username=email[:email.index("@")]
    domain=email[email.index("@")+1:]
    a=(f"username : {username} and domain : {domain}")
    print(a)

else:
    print("email does not contain spaces")