str=raw_input("enter a string")
for i in range(0,len(str)):
    if len(str)>=2:
        print(str[0:2]+str[-2:])
        break
    elif len(str)<2:
        print("empty string")
        
