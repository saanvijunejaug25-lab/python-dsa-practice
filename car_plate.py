def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    flag = 0

    # length check
    if 2 <= len(s) <= 6:
        flag += 1

    # first 2 letters
    if s[0].isalpha() and s[1].isalpha():
        flag += 1

    # only alphanumeric
    check = True
    for i in s:
        if not i.isalnum():
            check = False

    if check:
        flag += 1

    if flag == 3:
        return True
    else:
        return False

main()

