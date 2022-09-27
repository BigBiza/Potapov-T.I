import math
x=2.444
y=0.869*10**(-2)
z=-0.13*10**3
s=(x**(y+1)+math.e**(y-1))*(1+abs(y-x))/(1+x*abs(y-math.tan(z)))+abs(y-x)**2/2-abs(y-x)**3/3
print(s)