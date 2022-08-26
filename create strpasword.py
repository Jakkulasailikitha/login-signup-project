# print("welcome to the stong pass word world")
# user=input("enter your password here:")
# print(len(user))
# # charcter1=input("enter the lower case character :")
# # CHARACTER2=input("enter the upper case  character : ")
# # special_character=input("enter the special character  :")
# if len(user)>=8:
#     if user>="a" and user<="z" in user:
#         if user>="A" and user<="Z" in user:
#             if("special_character!=0") in user:  
#                 if user>="0" or user<="9" in user:
#                     print("strong password")
#                 else:
#                     print("numbers are missing")
#             else:
#                 print("special character is not there")
#         else:
#            print("upper case is not there")
#     else:
#         print("lower case is not there")
# else:
#     print("the password length should be long ")
    
    
    




password=input("enter the password")
if len(password)>=1 and len(password)<=10:
    if "@" in password or "#" in password or "$" in password:
        if password>="A" and password<="Z" in password:
            if password>="a" and password<="z" in password:
                if password>="0" or password<="9" in password:
                    print("strong password")
                else:
                    print("numbers are missing")
            else:
                print("small letter is missing")
        else:
            print("capital letter is missing")
    else:
        print("special character is missing")
else:
    print("your password is long")
    
    print("your password should be long")
    
