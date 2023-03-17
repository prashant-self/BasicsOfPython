#LIST TUTORIAL

#empty list
list1 = []
#print("empty list ", list1)

#list with items
list2 = [10, 20, 30, 40,50]
#print('list contains values ', list2)

#list with hetrogenous values
list3 = [10, 'ten', 20, 'twenty', 'p@#$r', 'p234r', '234rt', '*&%']
#print(list3)

list1.append('p@#$)')
#print(list1)
list1.append([10,20,30,40,50])
#print(list1)

list4 = []
list4.append(list1[0])
list4.append(list1[1][0])
list4.append(list1[1][1])
list4.append(list1[1][2])
list4.append(list1[1][3])
list4.append(list1[1][4])

#print(list4)
list5 = []
list5.append(list1[0])
list5.extend(list1[1])
#print(list5)

#print(list3[0])
#print(list3[1])
#print(list3[0:5])
#print(list3[:])
#print(list3[::2])
#print(list3[-8:-1:2])
#print(list3[::-1])
#print(list3[::-2])

list6 = [10, 'ten', 20, 'ten', 30, 'ten']
#list6[2] = 'twenty'
#print(list6)
#print(list6)
del list6[::-2]
#print(list6)

vowel = ['a', 'e', 'i', 'u']
#print(vowel)
vowel.insert(3, 'o')
#print(vowel)

num = [2, 3, 5, 7]
#print(num)
num.insert(5, 11)
#print(num)

pop_list = [10,20,30,40]
#print(pop_list.pop(0))
#print(pop_list)

#clear_list = [10,20,30,40]
#clear_list.clear()
#print(clear_list)

index_list = ['p','r','a','s','h','a','n','t']
#print(index_list.index('a'))
#print(index_list.index('a', 3))

count = ['a']
count_list = ['p','r','a','s','h','a','n','t']
count.append(count_list.count('a'))
#print(count)

sort_list = [11,3,7,5,2]
sort_list.sort()
print(sort_list)

import math
print(dir(math))


