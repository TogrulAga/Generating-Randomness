# put your python code here
integers = []
integers.append(int(input()))
while sum(integers) != 0:
    integers.append(int(input()))

print(sum(map(lambda x: x ** 2, integers)))
