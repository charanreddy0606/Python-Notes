'''
Coditional statements:
        this are block of statements whose execution depends on a certain condition.

types:
1.IF:
    a if condition is one where a block of statements get executed if the condition mentioned in the "if"
    statement evaluates to true.

2.If Else:
    An "If Else" statement is one where a block of statements under "if condition gets executed if the condition is true
    .if ithe condition is false, the block of statements under "Else" is executed.

3.if-Elif-Else:
    An "if-Elif-Else" statement is one where multiple if conditions are evaluated one after another
    if an "if" statement evaluates to false.if all the if conditions evaluates to false, the block statements
    under "Else" is gets executed.

4.Nested-if:

'''
totalmarks=39
if totalmarks >=90:
    print("congrats u have secured distinction")
elif totalmarks >=40 and totalmarks<=90:
    print(f"you have secured less than 90 marks .. i.e {totalmarks} you have secured ")

else:
    print(f"you have failed the  exam .. i.e {totalmarks} you have secured ")

#Nested IF

totalmarks1=100

if totalmarks1 >=90:
    print("congrats u have secured distinction")
    if totalmarks1 == 100:
        print("u have secured full marks")
elif totalmarks1 >=40 and totalmarks1<=90:
    print(f"you have secured less than 90 marks .. i.e {totalmarks1} you have secured ")

else:
    print(f"you have failed the  exam .. i.e {totalmarks1} you have secured ")


marks=92
attendance=90

if marks>=90 and attendance>=90:
    print("you r very diciplined student")

fruit = "apple"
if fruit is "mango" or fruit is "apple":
    print("i like that fruit")
