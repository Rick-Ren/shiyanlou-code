a=1
while a<=99:
    a+=1
    if a%7 ==0:
        continue
    elif a%10 ==7:
        continue
    elif a//10 ==7:
        continue
    else:
        print(a)
