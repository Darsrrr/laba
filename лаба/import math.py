import math

x = float(input("x: "))
if x < 1:
    f = x * math.sin(x)**2
elif x == 1:
    f = math.sqrt(x**5 + 15)
else:
    f = math.exp(x)
print("f =", f)
