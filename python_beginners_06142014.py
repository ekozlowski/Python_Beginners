"""
Questions from "Learning Python" by Mark Lutz
"""

# chapter 7:  String Fundamentals

# 1)  Can the string 'find' method be used to search a list? - No

hide = """
a = 'bob'
b = 'ed'
c = 'alisa'

my_list = [a,b,c]
for person in my_list:
    if person.find('ob') >= 0:
        print person



my_string = 'Ed'
print my_string.find('D')
"""

# 2)  Can a string slice expression be used on a list? Sure!

hide = """
my_string = 'ed was here'
print my_string[2:5]

my_list = [1,2,3,4,5]
print my_list[2:5]
"""

# 3)  How would you convert a character to its ASCII integer code?  How would
#     you convert the other way, from an integer to a character?
hide = """
import string

print chr(35)
print ord('a')
print str(unichr(97))
"""

# 4)  How might you go about changing a string in Python?
hide = """
'a' + 'b'
''.join(['a','b'])

attributes = {'name': 'ed', 'age': 24}
other_stuff = {'height': 54}
print 'My name is %s' % 'ed'

print 'My name is %(name)s, my age is %(age)d' % attributes

print 'My name is {name} and my age is {age}'.format(name='ed', age=24)

print 'My name is {0[name]} and my age is {0[age]}, {1[height]}'.format(attributes, other_stuff)
"""
# 5)  Given a string S with the value "s,pa,m", name two ways to extract
#     the two characters in the middle.

hide = """
import parse
s = 's,pa,m'
print s.split(',')[1]
print s[2:4]
print parse.parse('s,{name},m', s)
"""

"""
# Example of DictReader CSV
In [10]: dr = csv.DictReader(open('./ed.txt', 'r'))

In [11]: dr.fieldnames()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-3d2656af8767> in <module>()
----> 1 dr.fieldnames()

TypeError: 'list' object is not callable

In [12]: dr.fieldnames
Out[12]: ['person', 'age', 'country']

In [13]: dr.next()
Out[13]: {'age': '26', 'country': 'USA', 'person': 'ed'}

In [14]: dr.next()
Out[14]: {'age': '27', 'country': 'USA', 'person': 'alisa'}

In [15]: dr.next()
Out[15]: {'age': '42', 'country': 'Australia', 'person': 'joel'}

In [16]: dr.next()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-16-7db636840150> in <module>()
----> 1 dr.next()
"""

# 6)  How many characters are there in the string "a\nb\x1f\000d"?

# 7)  Why might you use the 'string' module instead of string method calls?



# chapter 8:  Lists and Dictionaries

# 1)  Name two ways to build a list containing five integer zeros.

# 2)  Name two ways to build a dictionary with two keys 'a' and 'b', 
#     each having an associated value of 0.

# 3)  Name four operations that change a list in place.

# 4)  Name four operations that change a dictionary in place.

# 5)  Why might you use a dictionary instead of a list?
