
# coding: utf-8

# DFW Pythoneers Beginners Hour - 2/13/2016
# =========================================
# 
# Topics We'll Cover Today
# ------------------------
# 
# - How this Demo is structured (I'm in Jupyter, or IPython Notebook)
# - How future "Beginners Hours" will be structured
# - Basic Code (Hello World!)
# - Variables and Types
# - Lists
# 

# # How This Demo Is Structured

# This is NOT typical Python.  We do not write Python in the browser.  (typically...)
# 
# Python code is typically written in a text editor, and saved to a file with a \*.py extension.  Python files do not have to be named with a \*.py extension.
# 
# What are .py files?
# .pyc?
# .pyo?
# 
# (From http://stackoverflow.com/questions/8822335/what-do-the-python-file-extensions-pyc-pyd-pyo-stand-for)
# 
# - .py: This is normally the input source code that you've written.
# - .pyc: This is the compiled bytecode. If you import a module, python will build a *.pyc file that contains the bytecode to make importing it again later easier (and faster).
# - .pyo: This is a *.pyc file that was created while optimizations (-O) was on.
# - .pyd: This is basically a windows dll file.

# # Basic Code  "Hello Python World!"

# In[ ]:

print("Hello Python Beginners Hour! Modify")


# The following snippet works in Python 2, but will not work in Python 3.  What do we get if we run it in Python 3?

# In[ ]:

print "Hello World!"


# # Variables And Types

# In[ ]:

age = 38  # Integer

pi = 3.141529 # float

also_a_float = float(7)

name = "Ed"  # String

also_a_string = """This is a string too!
testing
    does this indent
seperate lines?
"""

also_another_string = 'So is this!'

why_so_many_strings = """So 'you' can "do" 'fun' things like 'this'!"""
print(why_so_many_strings)
print(also_a_string)


# In[2]:

# Tuples
name, age = ('Ed', 38)
another_tuple = ('this', 1, {'dict': 'value'})
print("My name is {} and I'm {} years old.".format(name, age))


# In[3]:

# Tuples are "immutable"... That means you can't change them once they are set.
my_tuple = ('Ed', 38)
print(my_tuple[0])
print(my_tuple[1])


# In[4]:

# So what happens when we try?
my_tuple[0] = 'Alisa'


# In[8]:

# Namedtuples
# Notice above we did my_tuple[0], my_tuple[1]? 

# ...ugly, right?
# How about this?
my_tuple = ('Ed', 38)
print(my_tuple)
from collections import namedtuple
person = namedtuple('person', 'name, age')

# We'll just say that the other two tuples are "person" tuples...
my_tuple = person(my_tuple[0], my_tuple[1])
print(my_tuple)

print(my_tuple.name)
print(my_tuple[0])


# In[18]:

# You can also use the "positional expansion" operator if you want, and get the same thing.
p = ('Emily', 6)
emily = person(*p)  # all *p does here is expand p to (p[0], p[1])
print(emily)


def print_name(p):
    print("My name is {0.name} and I am {0.age} years old.".format(p))

print_name(emily)


# # Lists

# In[25]:

mylist = [1, 2, 3]
print(mylist)


# In[20]:

# There are lots of built-in methods that operate on lists
print("Sum is: {}.".format(sum(mylist)))

# You can see if something is "in" a list just by using the "in" operator.
print(3 in mylist)
print(4 in mylist)


# In[21]:

# this works for lists of strings too, or strings themselves...
print('ed' in 'education')
print('ed' in 'foo')
print('ed' in ['ed', 'alisa', 'emily'])


# In[22]:

# sometimes this gets a little wierd...
my_name = 'Edward'
print(list(my_name))


# In[35]:

# you can flip lists around
mylist = [4,3,4,5,2,3]
print(id(mylist))
mylist = sorted(mylist)  #< ---- Generates a *new* list.
print(id(mylist))
print(mylist)

print("in place sort")
print(id(mylist))
mylist.sort()
print(id(mylist))


# In[43]:

# this also works for strings, provided you convert it to a list first, then back...
my_name = 'Edward'
my_list_name = list(my_name)
print(my_list_name)
my_list_name.reverse()  # <---- NOTE:  This is an "in place" reversal.  No new variable is created.
print(my_list_name)
my_reversed_name = ''.join(my_list_name)
print('\t'.join(['a','b','c']) + '\n')
print(repr('\t'.join(['a','b','c'])))
print(my_reversed_name)


# In[44]:

# you can sort lists
mylist.sort()
print(mylist)


# In[45]:

# you can sort the lists reversed
mylist.sort(reverse=True)
print(mylist)


# In[46]:

# Unlike some other languages, in Python, lists do not have to be homogenous.
# The "type" of the object is determined at runtime.
mylist = ['Ed', 3, object(), {'This': 'is', 'A': 'dict'}]
print(mylist)


# In[47]:

# This means you can get into some trouble at runtime if you're not careful about your lists...
print(sum(mylist))


# In[76]:

foo(...)
def foo(name='default', hometown='default', age):
    print("Name: {} Age: {} Hometown: {}".format(name, age, hometown))

foo(age='38')


# In[79]:

print(myvar)


# In[83]:

def foo(a, b):
    print(a + b)


# In[85]:

def foo(a, b):
    print("foo is {} {}".format(a, b))


# In[86]:

foo(1,2)

