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
            
                
                    
            
        
    
    
    
        
        

        
                        
        
        
        
        
        
