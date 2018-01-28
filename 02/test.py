import itertools

possible = itertools.permutations("a,b,c,d,e,f,d", 7)
for x in possible:
  print(''.join(x).lower())
