Resources for Python Beginners
------------------------------

10 Resources To Learn Python:  http://codecondo.com/10-ways-to-learn-python/


Ned Batchelder's Presentation on Unicode:  https://www.youtube.com/watch?v=sgHbC6udIqc

If You Are On Windows
---------------------

ActiveState is a great distribution that I highly recommend.  I've used it for years.  You can download it at http://www.activestate.com/activepython/downloads  They do have a free edition, and business support is available if you need it.

If You Are On Mac
-----------------

Congratulations!  Python is built into Mac OSX!  However, you may run across people that swear by "brew installing" Python.  This is because if Apple updates Python, it may mess with anything third-party that you have installed if you use the system installed Python.  Brew installing Python gets around that.

If You Are On *nix
------------------

Congratulations!  Python is usually packaged with most \*nix installs!

My Personal Contact Info
------------------------

Edward Kozlowski
ekozlowski1@gmail.com

Please reach out with any Python related questions that I can help with!

Example Code (List Comprehensions and Generator Expressions
-----------------------------------------------------------

>>> my_list = [x for x in range(5)]
>>> my_list
[0, 1, 2, 3, 4]
>>> range(5)
[0, 1, 2, 3, 4]
>>> my_list = [x for x in range(5) if x > 2]
>>> my_list
[3, 4]
>>> my_list = (x for x in range(5) if x > 2)
>>> my_list
<generator object <genexpr> at 0x108bb1fa0>
>>> my_list.next()
3
>>> my_list.next()
4
>>> my_list.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

Ideas For Future Talks
----------------------

Python Packaging - Wheels Versus Eggs

