greet = input().title().strip()

if greet[0:5] == "Hello":
    x = 0
elif greet[0] == "H":
    x = 20
else:
    x = 100

money = x

print("$" + str(money))
