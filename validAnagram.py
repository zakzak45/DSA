def validAnagram(s,t)->bool:
    return sorted(t) == sorted(s)






s="mom"
t="mom"
print(validAnagram(s,t))
