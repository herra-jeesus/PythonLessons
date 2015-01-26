from modules import module as md

# Single Comment

"""
"""

'''
	Multiline comment
'''


integer = 2
if integer == 2:
	print "hey"
elif integer != 2:
	print "no"
else:
	print "nope"

while integer < 5:
	print integer
	integer = integer + 1

lst = [1, 2, "Hey"]

for item in lst:
	print item

for index, item in enumerate(lst):
	print index, item

def add(a,b):
	if a == 0 & b == 0:
		return 0
	else:
		return a + b
print add(3,4)

print md.add(10,10)

try:
	print "Borka" / 2
except NameError:
	print "Nope"
except:
	print "No"

fail = open('book.txt', 'r')

for line in fail:
	line = line.replace('\n', '')
	print line

fail.close()

fail = open('book.txt', 'a')
fail.write('Hello')
fail.close()

class className:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def add(self, a, b):
		return a+b

	def __del__(self):
		pass

obj = className(4,5)
print obj.add(10, 10)
print obj.a

boolean = True
boolean2 = False

'''
Function, accepts 2 parameters. 1 tuple, a list up tuples. 
Those tuples are (x,y) coordinates
First tuple is a playing field size.
The list is a set of coordinates.

field((5,5),[(1,1), (1,3)])

11211
1X2X1
11211
00000
00000
"""