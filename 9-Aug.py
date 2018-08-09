
#len() function is used to calculate the length of the string,list etc.
print(len("python"))   # -> 5

#-----MemberShip function (IN) is used to find a particular element----------#
print('D' in "DAnish")
#->True
print('d' in "Danish")
#->False

#-------------List-------------#
print('Apple' in ['Banana ','Apple','Grapes'])
#->True
print('Banana' in ['banana ','Apple','Grapes'])
#->False

#-------UserInput--------------#

name=input("your name plz")                     #prompt the user for entering input
print("Name = ",name)

#---------Statement------------#
#************IF****************#
a = 2
if a==10:                                                               #no parenthesis #no curly braces
    print("A is equal to 10 ")
elif a==9:
    print("A is equal to 9 ")
else :                                                                      #else is optional
    print("A is equal to 0")
    
#Else is optional

#----------PAlindrome----------#

word = input("Please  enter a word : ")
rev_word = word[::-1]                                                   #for getting he reverse of the string
if word == rev_word:
    print("Hooray!  You entered a palindrome")
else:
    print("you did not  enter a palindrome")



data = []                                                                           #empty list

if data:
    process(data)
else:                                                                                   #will perform else function as there is no data in data
    print("There is no data")

#---------FOR LOOP------

#range function is used to iterate over sequences of number
for i in range(5):          #for loop will iterate for 5 numbers 
    print(i)                     #-> 0,1,2,3,4 

for i in range(2,12,3):         #range(start,stop,steps)
    print(i)                                #-> 2,5,8

for i in range(-7,-30,-5):          #negative indexing will also work
    print(i)                                    #-> -7,-12,-17,-22,-27

#break breaks out of the smallest enclosing for or while loop

for n in range(10):
    if n==6:
        break
    print(n , end=',')

#continue continues with the next iteration of the loop
for n in range(1,10):
    if n%2==0:
        print("even",n)
        continue
    print("odd", n)


#-------functions:
#we use def keyword to define a function,parameter have no explicit types and return is optional
def add(a,b):
    c=a+b
    return c

print(add(3,4))             #Will print addition of 3 and 4 -> 7




#PRIME NUMBER FUNCTION
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input("Enter a number:"))               #by default input function return string value so if we have to type-cast it
for x in range(2,n):
    if is_prime(x):                                             #calling a function
        print(x,"is prime")
    else:
        print(x,"is not prime")




