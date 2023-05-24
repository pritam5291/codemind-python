s,k,res=input(),'aeiou',''
for i in range(len(s)-1):
    if s[i] in k and s[i+1] not in k:
        res+='V'
    elif s[i] not in k and s[i+1] in k:
        res+='C'
if s[-1] in k:
    res+='V'
else:
    res+='C'
print(res)
