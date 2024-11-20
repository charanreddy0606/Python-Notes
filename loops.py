'''
Loops:looping used for repeatedly perform a block of staements over and over again.

FOR lOOP:it is used to iterate over a sequence,starting from the first to the last.
        the number of iterations to be performed depends upon the length of the list.

While Loop:it is used for repeatedly execute a block of statements as long as condition mentioned
            in the whileloop holds true.

Nested Loop:a loop within another loop is called nested loop.the concept of loop could be a little bit of
            trouble understanding at first but can be simplified with an example.

Break:    it is used to stop the loop for further execution.

Continue: it is used to skip a particular iteration of the loop.

'''
fruits = ['aple',"orange","strawberry"]
for fruit in fruits:
    print(fruit)
for num in range(1,11):
    print(num)

temp=77
while temp>=68 and temp<=77:
    print(f"Room temp is maintained at  {temp} degree fahrenheit")
    temp= temp-1

'''for i in range(1,4):
    for j in range(i,4):
        print((i,j))'''
number=1
for i in range(1,4):
    for j in range(1,4):
        #print((i,j),end="  ")
        print(number,end="  ")
        number +=1
    print( )

for num1 in range(1,11):
    if num1 == 5:
        break
    else:
        print(num1)


for num1 in range(1,11):
    if num1 == 5:
        continue
    else:
        print(num1)









