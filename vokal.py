x = input().lower()
y = ["a", "i", "u", "e", "o"]
z = ''

for kcir in x:
    if kcir not in y:
        z += kcir

print(z)