#TUPLES##
#The are like list but are immutable types
# This means its data is easy to retrive coz its can't be changed
random_words=['water','land','tea','bed']
tuple_words=tuple(random_words)
print(tuple_words)
print(random_words)

#SETS
# carries a collection of items like lists but has no duplicate elements in it.
# Used in instances where the use of list would be inefficient like in:
# things like memmbership testing and duplicate entries elimmination.  
# created using the curly braces {} or the set() function. 

religions={'christians','muslims','christians','christians','hindus','budhism','muslims','greekGods'} 
unduplicated_religions=religions # the use if culry{} braces ensures that it returns an non-duplicated out-put.
print(religions)
