str5=raw_input("enter a string")
count=0
digit=0
#counter2=0
for i in range(0,len(str5)):
    if str5[i].isalpha():
        count+=1
    elif str5[i].isdigit():
        digit+=1
print("alphabets:",count)
print("digits:",digit)
