def factores(n):
 # factores de n > 0 natural
  f = []       
  if n > 1:
    f.append(1)
    t = n//2+1
    d = 2
    while d < t:
      c = n//d
      if n == d*c:
        f.append(d)
        if d < c: f.append(c)
        t = c-1
      d += 1

  return f

print(factores(12))