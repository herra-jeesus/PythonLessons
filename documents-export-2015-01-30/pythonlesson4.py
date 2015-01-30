class BaseClass(object):
	def __init__(self):
		self.x = 10
	def test(self):
		print("ham")


class InClass(BaseClass):
	def __init__(self):
		super(InClass, self).__init__()
		super(InClass, self).test()
		self.x = 20
	def test(self):
		print("hammer")
i = InClass()

print(i.x)
print(i.test())