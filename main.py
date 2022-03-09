nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

class Iter_item:
	def __init__(self,list):
		self.list = list
		self.flat_list = []

	def item_list(self):
		self.flat_list = []
		for item in self.list:
			if len(item) > 1:
				for it in item:
					self.flat_list.append(it)
			else:
				self.flat_list += item
		return self.flat_list


class Flat_iterator(list):
	def __init__(self,list):
		self.list = list
		self.elem = -1
		self.flat_item = []

	def __iter__(self):
		iter_item = Iter_item(self.list)
		self.flat_item = iter_item.item_list()
		return self

	def __next__(self):
		self.elem += 1
		if self.elem >= len(self.flat_item):
			raise StopIteration
		return self.flat_item[self.elem]


def flat_generator(list):
	elem = 0
	while len(list) > elem:
		for item in list[elem]:
			yield item
		elem += 1


flat_list_iter = [item for item in Flat_iterator(nested_list)]
print('Iterator')
print(flat_list_iter)
print('Generator')
for item in flat_generator(nested_list):
	print(item)
