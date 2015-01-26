lst = [1, 2, 3, 5]

# If gotcha
if 1 in lst:
	pass

# List sorting
lst = [(1,2,3), (3,1,1), (7,65,3)]
lst.sort(reverse = True, key=lambda x: x[1])
print lst

# Lambda
lamb = lambda x: x**2
print lamb(8)

# List comprehension
lst = [(x,y) for x in range(1,10) for y in range(1,20) if x==y]
print lst

def square(x):
	return x**2


# Generator
def generator():
	for x in range(1, 10):
		yield x

x = nex