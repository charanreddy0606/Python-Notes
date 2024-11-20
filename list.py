'''
list: it is used for collection of objects
listname = [o1,o2,o3]

'''
fruits=["apple","mango","banana"]
print(fruits)

print(type(fruits))
print(fruits[0])
print(fruits[-3])

fruits[1]="orange"
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"cherry")
fruits.sort()
print(fruits)

list1=["Zbc","Abc","bsd","012"]
list1.sort(reverse=True)
print(list1)

fruits.pop()
print(fruits)

'''for fruit in fruits:
    print(fruit)'''

