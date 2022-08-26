# random strong password created by themselves
# lower case=ascii_lowercase
# uppercase=ascii_uppercasse
# digits=digits
# symbols=punctuations
# these are in string module

# # import string
# # import random
# # len=int(input("enter the length of the password:"))
# # # lower=string.ascii_lowercase (having all the letters)
# # # upper=string.ascii_uppercase
# # # digit=string.digits 
# # # symbols=string.punctuation

# # # str=lower+upper+digit+symbols
# # str=string.printable
# # pwd=random.sample(str,len)
# # password="".join(pwd)
# # print(password)
# # # print(pwd)
# # # print(str) 




# # another method for random password  creating
# import string
# import random
# lower_len=int(input("enter the no.of lowercase character:")) 
# upper_len=int(input("enter the no.of upper case character:")) 
# digit_len=int(input("enter the no.of digits:"))
# symbol_len=int(input("enter the no.of symbols:"))
# pwd_len=lower_len+ upper_len+digit_len+symbol_len
# lower=string.ascii_lowercase
# upper=string.ascii_uppercase
# digit=string.digits 
# symbol=string.punctuation
# str=random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(digit,k=digit_len)+random.choices(symbol,k=symbol_len)
# random.shuffle(str)
# password=" ".join(str)
# print("password is:",password)

# # mystring = "Meet Guru99 Tutorials Site.Best site for Python Tutorials!"
# print("The position of Tutorials is at:", mystring.find("Tutorials"))



print("welcome to the stong pass word world")
charcter1=input("enter the lower case character :")
CHARACTER2=input("enter the upper case  character : ")
special_character=input("enter the special character  :")

num=int(input("enter the number")) 
if charcter1>="a" and charcter1<="z":
	  if CHARACTER2>="A" and CHARACTER2<="Z":
                 if("special_character!=0"):  
                    if"num>0 and num<=9":
	                    print("strong pass word")
else:
	  print("not pass word")