'''# 1.
tuple1 = ('Car', [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])

#2.
list1 = [44, 12, 578, 21, 134, 67]
print(list1[3:6])

#3.
list1 = [5, 10, 15, 20, 75, 100, 50]
print(list1.index(20))
list1[3] = 200
print(list1)

#4.
tuple1 = (11, [64, 33], 243, 123)
print(tuple1[1][1])
(tuple1[1][1]) = 66
print(tuple1)

#5.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))

#6.
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
print(list1[1:6:2])
print(list2[0:7:2])
list3 = (list1[1:6:2]) + (list2[0:7:2])
print(list3)
'''