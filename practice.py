import json
print("LoginSystem @mvtthis")
myRL = input("Login or Register?")
if myRL == "Register":
    User = input("Username:") 
    PW = input("Password:")
    PW1 = input("Confirm Password:")
    if(PW == PW1):
        print("Registration successfully.")
        with open('LoginSystemData.json', 'a') as f:      
                f.write("\n" + User + "," + PW)        
    else:
        print("Registration failed! Please confirm your Password correctly.") 
if myRL == "Login":
    User = input("Username:") 
    PW = input("Password:")
    success = False
    with open('LoginSystemData.json', 'r') as f: 
        for i in f:
            a,b = i.split(",")
            b = b.strip()
            a = a.strip()
            if(a==User and b==PW):
                print("Login successful")
            else:
                print("Login failed. Wrong Username or Password.")     
            f.close() 
            break