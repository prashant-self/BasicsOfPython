#list1 = [100,200,300,400,500]
#list1.reverse()
#print(list1)

#list1.sort(reverse=True)
#print(list1)

#print(list1[::-1])

#value = 1
#reverse_list = []

#for i in list1:
#	if i > value:
#		reverse_list.append(i)
#print(reverse_list)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list4 = [i + j for i, j in zip(list1,list2)]
#print(list4)

#output:-- ['My', 'name', 'is', 'Kelly']

list3 = []

list3.append(list1[0] + list2[0])
list3.append(list1[1] + list2[1])
list3.append(list1[2] + list2[2])
list3.append(list1[3] + list2[3])

#print(list3)

#numbers = [1, 2, 3, 4, 5, 6, 7]

#square = []

#for i in numbers:
#	square.append(i*i)
#print(square)

#res = [i*i for i in numbers]
#print(res)


# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# res = [x + y for x in list1 for y in list2]
# print(res)
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# list1.insert(list1[3][2], 7000)
# print(list1)

import math
char = 'pra2sha8nt7su&%'
digits = []
digits.append(int(char[3]))
digits.append(int(char[7]))
digits.append(int(char[10]))

p =sum(digits)

print(p)
c = p/3
print(c)

