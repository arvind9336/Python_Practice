# What is tuple
# Ans: A tuple is an immutable ordered collection of element
# Tuple are similar to list, but unlike list they can not be changed after their creation.
# can hold element of different data types
# These are ordered, hetrogeneous and immutable.






def sumofIndex(t):
    c=0
    for i in range(len(t)):
        c=c+i
    return c
t1=(1,2,3,4,5,6)
print(sumofIndex(t1))