l = [1,3,5,6,8]
cnt = 0
for i in l:
    for j in l:  #this is a valid way to run the code but we have O(n^2) here not prefered
        if i+j == 9:
            cnt +=1
print(cnt)
# using 2 pointer technique to reduce time complexity
def find_two_number(number, target):
    left = 0
    right = len(number) - 1
    while left<right:
        total = number[left] + number[right]
        if total == target:
            return number[left], number[right] # here time complexity is O(n) but numbers in list should be sorted 
        elif total>target:
            right = right -1
        else:
            left = left + 1
    return []
numbers = [6,3,1,4,5,9]
numbers.sort()
s1 = find_two_number(numbers, 9)
print(s1)