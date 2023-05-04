# You can convert from one type to another with the int(), float(), and complex() methods

x = 4  # int
y = 4.5  # float
z = 4j  # complex

# int -> float
a = float(x)

# float -> int
b = int(y)

# int -> complex
c = complex(x)

print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))
