camel_case = input("enter name in camel's case")
snake_case = []
for i in camel_case:
    if i.isupper() == True:
        snake_case.append("_"+i.lower())
    else:
        snake_case.append(i)

print("".join(snake_case))
