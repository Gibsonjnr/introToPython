#day 2

#String

Name = "Shine"

name2 = """ 
 person1 , person2 ,person3,

 person4
"""

print(name2)


func = "Shine"
print(f"Hello {func}")

print(len(func))
print(func.lower())
print(func.isalpha())


test = "Hello Agent 22"
print(test.isalpha())

print(test.isalnum())
print(test.isprintable())
print(test.endswith(' '))


testRun = "Gibson"

print(testRun.replace( 'son' ,'by'  ))

print(testRun[-2])
print(testRun[-3])

print(testRun.find('Y'))


complexNum = 5 + 6j

print(complexNum.real)

number = -6
number1 = 4.334567
print(abs(number))
print(round(number1 , 4))


import math

print(math.pi)
print(math.tan(4))

print(bool(''))


lists = ["Shine" , "Ben" , 'Dan']

lists[2] = "Bright"

print(lists)
print(lists.index('Ben'))
#del lists[0]
print(lists.pop(1).upper())
print(lists)


#Control Structure
