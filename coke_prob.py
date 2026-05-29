Amount_due = 50
print(Amount_due)
while Amount_due != 0:
    coin = int(input("enter coin of denomination 25, 10, 5"))
    if coin == 25:
        balance = Amount_due - 25
        Amount_due = Amount_due - 25
        print(Amount_due)
        print(balance)
    elif coin == 10:
        balance = Amount_due -10
        Amount_due = Amount_due - 10
        print(Amount_due)
        print(balance)
    elif coin == 5:
        balance = Amount_due -5
        Amount_due = Amount_due - 5
        print(Amount_due)
        print(balance)
    else:
        pass
if Amount_due == 0:
    print("done")
