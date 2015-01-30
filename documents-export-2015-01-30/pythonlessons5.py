from abc import ABCMeta, abstractmethod

class BaseClass(object):
	__metaclass__ = ABCMeta

	@abstractmethod # Decorators
	def __init__(self):
		d='lol'
		print(locals())
		#print(globals())

class InClass(BaseClass):
	def printHam(self):
		print("Ham")
	def local(self):
		super(InClass, self).__init__()

i = InClass()
i.printHam()
i.local()