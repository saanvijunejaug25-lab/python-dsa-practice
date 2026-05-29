name = input("enter ")
final = []
vowels = ['a', 'e', 'i', 'o', 'u']
for i in name:
    if i in vowels:
        continue
    else:
        final.append(i)
print("".join(final))
