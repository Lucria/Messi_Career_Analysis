# Create a string variable 
# Create a integer variable
# Print the string varaible * integer variable
restaurants = "Burger King"
nums = 78
print(nums*restaurants)

print("nums*restaurants")
print('asdf')
print("asdf")
print("")


#################################################
# Logical Operators

test1 = 5 > 3 # True
test2 = 5 < 3 # False
print(test1)
print(test2)
print("")
print(test1 and test1) # True
print(test1 and test2) # False
print(test1 or test2) # True
print(test2 or test2) # False

# And
# T T = T
# T F = F
# F T = F
# F F = F

# Or
# T T = T
# T F = T
# F T = T
# F F = F

#################################################
print("")

# If hours <= 40, pay = hours * rate
# If hours > 40, pay = hours * rate * 2
print(str(10))
print(int("10"))

rate = 74
hours = 45

if hours <= 40:
    pay = hours*rate
else: 
    pay = hours*rate*2

print(pay)
print("")
#################################################


nums = range(1, 101, 2)
for i in nums:
    print(i)


print("")
#################################################

list1 = [0, 1, 2, 3, 4, 5] # range(0, 6)

list3 = list1[:] # copy the list 
list4 = list1[2:] # 2, 3, 4, 5 
list5 = list1[:4] # 0, 1, 2, 3
print(list3)
print(list4)
print(list5)
print("")

#################################################

# 1 2 3
# 4 5 6
# 7 8 9

m = [[1,2,3],[4,5,6],[7,8,9]]
s = i = 0
size = 3
while i < size: # i is column
    j = 0 # j is row 
    while j < size:
        s += m[j][i] # It will go down by each row
        j += 1
    print(s, end=' ')
    i += 1
