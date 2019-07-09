def jisuanqi(left,right,T):
    a = left
    b = right
    if T == "+":
         ret = a+b
    elif T == "-":
        ret = a - b
    elif T == "*":
        ret = a * b
    elif T == "/":
        ret = a/b
    else:
        print("qewqewq")
    return  ret
r=jisuanqi(5,5,"2")
print(r)