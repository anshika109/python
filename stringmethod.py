str1="hello world"
word="one fish,two fish,red fish,blue fish"
print("capitailse():",str1.capitalize())
print("count():",str1.count("l"))
print("count():",str1.count("l",3,7))
print(word.count('fish'))
print("title():",str1.title())
prophecy="there shall in that time"
counter=0
a=prophecy.count("a")
b=prophecy.count("e")
c=prophecy.count("i")
d=prophecy.count("o")
e=prophecy.count("u")
counter=a+b+c+d+e
print("vowels are",counter)
str2="welcome to the world of python"
print("endswith():",str2.endswith("python"))
str3="to"
print("endswith():",str2.endswith(str3,2,15))
print("islower():",str2.islower())
print("islower():",str1.islower())
print("isalpha():",str2.isalpha())
str4="Pyhton47"
print("isalnum():",str4.isalnum())
str5="1234"
print("isdigit():",str5.isdigit())
print("isupper():",str4.isupper())
str6=" "
print("isspace():",str6.isspace())
print("find():",str1.find(str3))
str7="world"
print("find():",str1.find(str7))
print("find():",str1.find(str7,2,11))
print("format()","sum of 1+2 is{0}".format(1+2))
print("format():","sum of {0} +{1} is {2}".format(1,2,3))
print("len():",len(str1))
print("lower():",str1.lower())
print("startswith()",str1.startswith("hello"))
print("startswith()",str1.startswith("wo",2,16))
str8="Welcome to PYTHON"
print("swapcase()",str8.swapcase())
str9="9999hello9999"
print("rstrip()",str9.rstrip('9'))
print("join()","-".join(str9))













