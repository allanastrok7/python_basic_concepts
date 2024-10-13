# We now move to ####LISTS####
# Are a type of sequence (like strigs,dict....etc)
# Are mutable(can be changed)
# Has various methods for performing for manipulating items in a list such as:
#APPEND METHOD
house_bratheon=[]
house_stark=['arya','catlyn','sansa','Rob','Lordstark']
house_stark.append('jhonsnow')  
print(house_stark)

house_stark[1]  # get the pst of the item in a list using indexing
dead_starks_sn3=[house_stark[1],house_stark[3]]
dead_starks_sn1=[house_stark[-2]]
dead_starks_sn6=[house_stark[-1]]
dead_starks=[]+dead_starks_sn1+dead_starks_sn3+dead_starks_sn6 # performing addition operations in Lists
#dead_starks_sn1
#dead_starks_sn1.append('lordstark')
print(dead_starks_sn3)
print(dead_starks_sn1)
print(dead_starsks)   #an example in how you can create another list from the original one.

#INSERT METHOD
#Used to add an items to a list at specific location.
lordstraks_kids=['Rob','Bran','Arya',]
lordstraks_kids.insert(1,'sansa') # the insert method add items at a specified position
lordstraks_kids.insert(len(lordstraks_kids),'jhonsnow') # works the same way like the .append method
print(lordstraks_kids)
#REMOVING ITEMS FROM A LIST
#Use the pop([]) and the remove methods
numbers=[1,2,3,4,5]
numbers.remove(numbers[2])
print(numbers)

nums=list(range(1,100))
removed_num=nums.pop() # pop method allows you to remove an items and store it 
print(removed_num)  #so that you can return it later on when you will need it
print(nums)
#REVERSE AND SORT() METHODS
drink_types=['water','beer','juice','sodas','porridge']
drink_types.reverse() # literally reverses them without sorting first
print(drink_types)
#SORT METHOD
digits=[1,3,4,7,8,9,3,5,2]
digits.sort() # sorts them in eithe ascending or descending order
digits.sort(reverse=True)
print(digits)
#LIST COMPREHENSIONS (A fancy way of creating list)
#using the lambda expression
square=list(map(lambda x:x**2,range(1,10)))
print(square)

# Creating a LIST from inputed string literals
your_fav_actor=(input("Please enter your Favourite GOT character: ")) #type in your GOT fan in the terminal when given the prompt
print(your_fav_actor) # will return a string literal
best_actors=[] #you cant add the input of y directtly intto the string coz it comes as a string and can't add [] + string together. 
best_actors.append(your_fav_actor) #use append instead.
print(best_actors)