# Are a group of compund statements that controls the flow of objects
# Made up of a clause (A header statement and suite)

# wew will still be using #Got characters in our code.

#########################################################################################################################

## THE WHILE LOOP ###
#the while loop executes a program as long as its true.

# an example using the Fibonacci series
a,b= 0,1
while a<10: # this the first part of the clause, the header statement.
 # in-oder of ecxecutions, the first suite print the intial value of a
 print(a)
 # second suite the updates the value of a and b repectively
 a,b=b,a+b
 
#######################################################################################################################
 
### The If-Statements ###
# x=int(input('Input an interger: ')) #Activate this if you want to know how input function works.
x=880
if x<10:
    print('Negative changed to zero')
elif x==0:
    print('Number is Zero')
elif x==17:
    print('Seventeen')
else:
    print('More')

#You can make the above if_statement shorter by excluding the elif block and going straight for the else  block.
dead_stark_sn1='Lordstark'
if dead_stark_sn1=='Lordstark':
    print("Correct")
else:
    print("Incorrect")

#######################################################################################################################

### For-Loops ###
#for-loops goes through or loops through an entire sequence then returns an output of each item.

got_dragons=['Drogon','Viserys','Arraxys','Balerion']
for dragon in got_dragons:
    print(dragon, len(dragon))
    
### THE RANGE() FUNCTION ###
#used to generate a sequence of numbers in loops and iterations
# can be written in various ways
for i in range(5):
    print(i)

for i in range(1,50):
    print(i)

for i in range(1,10,2): #the third command makes the range return values from one at an increament of 2 for the subsequent values. 
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#match statements
#the break and continue statement
#pass and match statements
