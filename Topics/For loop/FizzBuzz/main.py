for i in range(1, 101):
    msg = ""
    msg = "Fizz" if i % 3 == 0 else ""
    msg += "Buzz" if i % 5 == 0 else ""
    print(msg if len(msg) > 0 else i)
