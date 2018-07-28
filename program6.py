n=raw_input("enter a string")
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i in vowel:
        print(i,"is vowel")
    else:
        print(i,"is consonant")
