x = [7, 12, 9, 4, 11]

minvalue = x[0]

for i in x:
    if i < minvalue:
        minvalue = i

print("lowest", minvalue)

x.append(3)
x.remove(12)
x.pop(3)

print(x)

x.sort()
print(x)

y = [1, "hello", 3.1419, 36, 8738, True]

print(y)

z = [43, 48, 91, 31, 37, 28, 72]

print(z)

print(z[2])
print(z[2:6])

print(z[-1])
print(z[-3])
print(z[-5:-2])

z[3] = 44
print(z)

z[2:3] = [33, 43, 53]
print(z)

z.insert(2, 100)
print(z)

z.reverse()
print(z)

print(len(z))
print(max(z))
print(min(z))
print(z.count(43))
print(z.index(43))