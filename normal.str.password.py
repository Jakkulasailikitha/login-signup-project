print("welcome to the stong pass word world")
charcter1=input("enter the lower case character :")
CHARACTER2=input("enter the upper case  character : ")
special_character=input("enter the special character  :")
num=int(input("enter the number")) 
password=str(charcter1)+str(CHARACTER2)+str(special_character)+str(num)
if len(password)<=8:
    if charcter1>="a" and charcter1<="z" in password:
        if CHARACTER2>="A" and CHARACTER2<="Z" in password:
                if("special_character!=0") in password:  
                    if num>="0" or num<="9" in password:
                        print("strong password")
                    else:
                        print("numbers are missing")

                else:
                    print("special character is not there")
        else:
            print("upper case is not there")  
    else:
        print("lower case is not there")
else:
	  print("password length is long")