a = open("demofile.txt")
print(a.read())
a.close()

with open("demofile.txt") as a:
    print(a.read())

a = open("demofile.txt")
print(a.read(5))
a.close()

a = open("demofile.txt")
print(a.readline())
a.close()

a = open("demofile.txt")
print(a.readline())
print(a.readline())
a.close()

a = open("demofile.txt")
for x in a:
    print(x)
a.close()

a = open("demofile.txt", "w")
a.write("Hello areesha\n")
a.write("I am learning Python")
a.close()

a = open("demofile.txt")
print(a.read())
a.close()