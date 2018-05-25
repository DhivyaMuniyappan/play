a,b=map(int,input('').split(' '))
f=1
ff=1
for i in range(1,a+1):
  f=f*i
for i in range(1,b+1):
  ff=ff*i
print(round(f/ff))
