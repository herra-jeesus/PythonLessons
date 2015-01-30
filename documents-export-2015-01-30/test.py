def fun(a, *args, **kwargs):
	print(kwargs['yes'])
	for key, value in kwargs.items():
		print(key, value)
	for value in args:
		print(value)

fun('test','hello', yes = 'tere', no = 2)

class D(object):
	pass

class B(D):
	pass
class F(object):
	pass

class C(D, F):
	pass

class A(B, C):
	pass

print(A.__mro__)