import json
user=input("enter login or signup :")
if user=="signup":
    user_name=input("enter the user_name :")
    password=input("enter the password here : ")
    print("enter your conformation password")
    conformation_password=input("enter the conformation password :")
    if len(password)>=1 and len(password)<=17:
        if "A" or "Z" in password:
            if "@" in password or "#"in password or "$" in password:
                if "a" or "z" in password:
                    if "0" or "9" in password:
                        print("strong password")
                    else:
                        print("week password")
                else:
                    print("lower case is not there")
            
            else:
                print("special character is not there")
        else:
            print("upper  case is not there")
    else:    
        print("wrong password")
    if password==conformation_password:
        pass
        with open ('Signup.json'):
            b=open('Signup.json',"r")
            data=json.load(b)
            for i in data["user"]:
                if i["user name"]==user_name:
                    print("it's already exists")
                else:
                    dict={}
                    d={}
                    dict["user name"]=user_name
                    dict["password"]=password
                    d["description"]=input("enter the description here:")
                    d["date of birth"]=input('enter the date of birth:')
                    d["gender"]=input("enter the gender here:")
                    d["Hobbies"]=input("enter your hobbies :")
                    dict["profile"]=d
                    b=data["user"]
                    b.append(dict)
                    f=open("signup.json","w")
                    json.dump(data,f,indent=4)
                    f.close()
                    print("sigup succesfully")
                    break

    else:
        print("does not match")
elif user=="login":  
    b=open("signup.json","r")
    f=json.load(b)
    c=input("enter the user name for login:")
    d=input("enter the password for login:")
    for i in f["user"]:
        if c==i["username"]:
            if d==i["password"]:  
                print("login sucessfully")
                print(i)
            else:
                print("check your password")
        else:
            print("check your username")
            break
else:
    print("check your pin number")


# import json
# user=input("enter signup or login:")
# if user=="signup":
#     user_name=input("enter the name")
#     password1=input("enter the password1:")
#     print("please confirm your password")
#     password2=input("enter the password2:")
#     if len(password1)>=1 and len(password1)<=16:
#         if "@" in password1 or "#" in password1 or "$" in password1:
#             if "A" or "z" in password1:
#                 if "0" or "9" in password1:
#                     print("strong password")
#                 else:
#                     print("week password")
#             else:
#                 print("weekly password")
#         else:
#             print("nothing")
#     else:
#         print("wrong password")
#     if password1==password2:
#         pass
#         with open ('Signup.json'):
#             a=open('Signup.json',"r")
#             data=json.load(a)
#             for i in data["user"]:
#                 if i["username"]==user_name:
#                     print("Already Exists")
#                 else:
#                     dict={}
#                     d={}
#                     dict["username"]=user_name
#                     dict["password"]=password1
#                     d["Description"]=input("enter Description : ")
#                     d["D.O.B"]=input("enter Date Of Birth : ")
#                     d["Gender"]=input("enter your gender : ")
#                     d["Hobbies"]=input("enter your Hobbies : ")
#                     dict["Profile"]=d
#                     a=data["user"]
#                     a.append(dict)
#                     f=open("Signup.json","w")
#                     json.dump(data,f,indent=4)  
#                     f.close()
#                     print("Signup Succesfully")
#                     break
#     else:
#         print("doesn't match")
# elif user=="login":
#     a=open("Signup.json","r")                 
#     f=json.load(a)
#     b=input("Enter your user name for login:")
#     c=input("Enter your password for login:")
#     for i in f["user"]:
#         if b==i['username']:
#             if c==i['password']:
#                 print("Login successful")
#                 print(i)
#             else:
#                 print("Check your password")
#                 break
#         else:
#             print("Check your user_name")
#             break
# else:
#     print("Your enter worng input ")
            
                
                    
            
        
    
    
    
        
        

        
                        
        
        
        
        
        
