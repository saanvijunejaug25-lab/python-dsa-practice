marks = [22, 43, 49, 50]
print(marks[0]) # time complexity = O(1)
def find_names(names, target):
    left = 0
    right = len(names)-1
    while left<=right:
        middle =( left + right)//2 # Binary search time complexity = O(log n) because the search space is halved each iteration
        if names[middle] == target:
            return middle
        elif names[middle] < target:
            left = middle + 1
        elif names[middle]>target:
            right = middle- 1
    return -1
names = ['priya', 'rohan', 'saanvi', 'shourya']
target = "priya"
s1 = find_names(names, target)
if s1 == -1:
    print("not found")
else: 
    print(s1)

def exam(name, r):
    for i in name:
        if i == r:# here time complexity is O(n) since we are usinf one for loop
            return True
    return False
name = ['sagar', 'rachna', 'chirag' , 'rahul', 'archana']
r = "rachna"
s2 = exam(name,r)
if s2 is True:
    print("found")
else:
   print("not found")

def duplicate(check):
    for i in range(len(check)):
        for j in range(len(check)):
            if i != j and check[i] == check[j]: # here time complexity is O(n^2) since 2 loops are being used
                return True
    return False
            
check = [12,13,12,14,15,16]
s3 = duplicate(check)
if s3 is True:
    print("duplicate")
else:
    print("no duplicate")




    

