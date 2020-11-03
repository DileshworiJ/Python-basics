#executingassignmentstatements

width = 17
height = 12.0
delimiter = '.'



print("value of width/2:", width/2)
print("type of Expression", type(width/2))

print("\nvalue of width/2.0:", width/2.0)
print("type of Expression", type(width/2.0))

print("\nvalue of height/3:", height/3)
print("type of Expression", type(height/3))

print("\nvalue of 1+2*5:", 1+2*5)
print("type of Expression", type(1+2*5))

print("\nvalue of delimiter*5:", delimiter*5)
print("type of Expression", type(delimiter*5))



#converting fahrenheit to celsius in degerees
##
f = float(input("Enter Temperature in fahrenheit: "))
fc = (f -32)*5/9
print("The Temperature", f,"F converted into celsius is:",fc)

#conversion into minutes and seconds
s = float(input("enter the second: "))
m = s/60
ss = s%60
print("%.2f Second results in %.2f minutes and %.2f seconds" %(s,m,ss))


#list of an arbitrary element
fruits = ['apple', 'banana', 'cranberry', 'dragon fruit', 'erdberre']
print("\nLength 0f the list", len(fruits))
print("First element of the list is", fruits[0])
print("Fourth element of the list is", fruits[3])
print("original list", fruits)

#list methods
#append
fruits.append('fig')
#pop
print("\nBefore popping out:", fruits)
print("Pop:", fruits.pop())
print("After popping a element:", fruits)

#insert
print("\nInsert element at 3:", fruits.insert(3, 'date'))
print("list after inserting:", fruits)
print("remove", fruits.remove('date'))
print("list after removing:", fruits)


