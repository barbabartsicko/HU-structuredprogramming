# while loop andere kant
i = 1
lengte = int(input("hoe groot ?"))
while i < lengte:
    print(' ' * (lengte - i) + "*" * i)
    i += 1
while i > 0:
    print(' ' * (lengte - i) + '*' * i)
    i -= 1

# for loop andere kant
i = 1
lengte = int(input("hoe groot ?"))
for i in range(lengte):
    print(' ' * (lengte - i) + "*" * i)
i = 0
for i in range(lengte):
    print(' ' * i + "*" * lengte)
    lengte -= 1

#while loops
i = 1
lengte = int(input("hoe groot ?"))
while i < lengte:
    print("*" * i)
    i += 1
while i > 0:
    print('*' * i)
    i -= 1

#for loops
i = 1
lengte = int(input("hoe groot ?"))
for i in range(lengte):
    print("*" * i)
i = 0
for i in range(lengte):
    print("*" * lengte)
    lengte -= 1
