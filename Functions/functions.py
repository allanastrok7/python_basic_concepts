# A function is basically a package of procedures that can be reused multiple times.
# Helps you to reuse code avoiding copying and pasting that causes code reduancy in your python program
# Pythons functions comes in sets:
# Functions can be written in either of this two ways:{using def(), and lambda()}


# WRITING FUNCTIONS
# There are two ways used to send results back to user or return output of a function: {Using the return and yeild(print) keywords} 
# An example of a functions used to perfom a fibonacci series operation
# This is type of function that performs a task (cos of the use of yield keywords)

def fib(n):
    a,b=0,1
    while a< n:
        print(a, end=' ') # the end='' allows you to print items on the same line
        a,b=b,a+b
    print()    
fib(2000)

#PARAMETERS IN FUNCTIONS
# The function takes in parameters which will enables you to pass later on pass arguments.
# The arguments you pass allows you to know how the control the output of the function.

def greet(first_name,last_name): # the parameters
    print(f"Hello {first_name} {last_name}")
    print("Welcome Aboard")
greet("Allan","Alekey") # Argument 1
greet("Bran","theGreat") # Argument 2

# First two functions used above are of perfom a task
# Another types of a function is that which returns a value
dead_got_actors={'house_stark':'lord_stark', }
def dead_got_characters(actor_name,house_name, died_by='beheading'): # the last parameter can have a default value to be used if an argument is not passed
    for char in actor_name:
        if actor_name=='lordstark':
            return f"True {actor_name}'s death of house {house_name} was a horrid one. Killed through {died_by}"
        if actor_name=='geofrey':
            return f"""Yes King {actor_name} of the house {house_name} died a horrible death;{died_by} Deserved it though"""
        else:
            return print(f"""Din't know {actor_name} died from {died_by} so sad to hear that""") # the print function changes the output

dead_got_characters("lordstark","stark","beheading")
dead_got_characters("geofrey","baratheon")
dead_got_characters("geofrey","baratheon","poisoned by the Queen of thorns")
dead_got_characters("catlyn","stark",'cut to the throat')

#DEFAULT ARGUMENTS# in python has vatrious applications for example:
# this simple fn wants to find out if the person or user is ok

def is_user_ok(prompt,retries=4,reminder="Please try again"):
    response=input(prompt)
    if yes in response:
        return true
    else:
        return false
is_user_ok("yes")
is_user_ok('n')
        
# when are default arguments in python created?
# they are created immediately the function is declared not when the function is being called
#as such the result if the code below is 5 and not 6                
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# Functions that return values are flexible because you can store them in a variable to be used when called upon
# The following function works like the built in function of len() to print out the length of a string.
def string_len(s):
    count=0
    for len in s:
        count+=1 #a short form of count=count+1
    return count  
my_string=string_len("water")
print(my_string)

#modifiying the above code of fibonacci series so that its returns a value and add the value to a list. 
def fib_series(numbers):
    result=[]
    a,b=0,1
    while a <numbers:
        result.append(a)
        a,b=b,a+b
    return(result)

new_fb_series=fib_series(1000)
print(new_fb_series)        
    
    
#MULTIPLE ARGUMENTS IN PYTHON
# we use the following syntaxes *argument & **argument

def numbers(*nums):
    total=1
    for digit in nums:
        total*=digit
    return(total)
numbers(1,5,4)

#creating a dictionary item using the double ** arsterik
def fav_got_character(**got_member):
    print(got_member) 
    #to get a specific value from the dictionary:
    print(got_member["name"])
    
fav_got_character (name="JhonSnow",house_name='Housestark', real_name='Kit Harrington', age=(2024-1986), other_info='English Boy')

#KEY-WORD AND POSITIONAL ONLY ARGUMENTS
#they determine how you will pass arguments to your python code
# Below is a diagram that explains types of arguments in relation to where they are placed in a functions

print("""
      
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
      
           
    """)

                 
def normal_arg(name,age):
    print(age)
normal_arg("allan",20)

def normal_arg(name,*,age):
    print(age)

normal_arg("allan",age=20)
normal_arg("allan",20)

#SCOPE VISIBILITY#
# A scope is a region of the code where a variable is defined
# we have global and local scopes.
# Scope visibility in python's function refers to how you can access and change the variables in the functions.
# Scope visisbilty Done in two ways: 
# Using the global() scope from variables outside the function and,
# Using the the nonlocal scope for nested functions:

message="hello" # global variable accessible outside the function
def greet(name):
    message="hi" # local variable accesible only inside this function
    print(message)
greet("mosh")
print(message)

#LAMBDA EXPRESSIONS in python
#used to create small functions without names.
#Are ussually one line
square=lambda x: x+2
print(square(5))
# Can take multiple arguments.
subtract=lambda x,t:x-t
print(subtract(10,5))


def greet(name: str) -> str:
    """
    This function takes a name as input and returns a greeting message.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"
greet()