x = input().lower()
y = ["a", "i", "u", "e", "o"]
z = ''

for _ in x:
    if _ not in y:
        z += _

print(z)
