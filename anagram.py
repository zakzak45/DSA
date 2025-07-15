def anagram(t,s):
  if len(t)!=len(s):
    return False
  return sorted(t)==sorted(s)





t="mmo"


s="mom"


print(anagram(t,s))