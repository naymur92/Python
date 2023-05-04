a = str('Hello')
print(a, "->", type(a))

b = int(23)
print(b, "->", type(b))

c = float(34.2)
print(c, "->", type(c))

d = complex(1j)
print(d, "->", type(d))

e = list(("Apple", "Banana", "Chery"))
print(e, "->", type(e))

f = tuple(("Apple", "Banana", "Chery"))
print(f, "->", type(f))

g = range(3)
print(g, "->", type(g))

h = dict(name="Naymur", age=30)
print(h, "->", type(h))

i = set(("Apple", "Banana", "Chery"))
print(i, "->", type(i))

j = frozenset(("Apple", "Banana", "Chery"))
print(j, "->", type(j))

k = bool(4)
print(k, "->", type(k))

l = bytes(5)
print(l, "->", type(l))

m = bytearray(5)
print(m, "->", type(m))

n = memoryview(bytes(5))
print(n, "->", type(n))