number = int(input())

if number > 1 and all(number % x != 0 for x in range(2, number)):
    print("This number is prime")
else:
    print("This number is not prime")
