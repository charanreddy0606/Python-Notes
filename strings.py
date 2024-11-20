'''
string name = "string" or 'string'

A  P  P  L  E
0  1  2  3  4
-5 -4 -3 -2 -1


FString :
it is an shortform formatted in string literals were introdeced in py 3.6 .
they r creating with prefix "F/f" and using curly brackets to insert
 expressions , variables,function calls.
'''
fruit= "APPLE"
print(fruit[0])
print(fruit[-3])

#print(fruit[6])  out of range

string1='string is one  among python\'s data  ' #  \ is executioned to avoid the quotes in the sentence
print(type(string1))
print(string1)

pgmlang="python"
print("pgmlang is a great program language")
print(pgmlang," is a great program language")


print("{} is a great program language" .format(pgmlang))

demo="hello , {} you are {} Years old "#.format("cherry",222)
print(demo)
newdemo=demo.format("vijay",30) #doubt
print(newdemo)


name="Cherry"
age=25
#fstring
test= f"hello,{name}, you are {age} years old "
print(test )

string2="python programming is easy"
b=string2.upper()
print(b)
print(b.lower())

c=string2.replace("easy","powerful") # to replace the string we use the replace
print(c)
print(len(string2))
print(string2[0:6])

