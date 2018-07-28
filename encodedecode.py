str1="hello"
print("encode()",str1.encode('utf-8','strict'))
str1=str1.encode('base-64 ','strict')
print(str1)
str1=str1.decode('utf-8','strict')
print(str1)
str2="hello/tworld"
print(str2.expandtabs(16))
print(max("hello"))
print(min("hello"))
str3="this is a string.this is vice"
print(str3.replace("is","was"))
print(str3.replace("is","was",3))
str4="welcome \nto \nworld \nof \npython"
print(str4.split())
print(str4.split(' ',2))

        
    
    
