email=input("enter your email=")
index=email.index("@")
print("Domain= ",email[:index])
print("Mailused= ",email[index+1:])