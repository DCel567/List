
class Node:
	def __init__(self, value=None):
		self.value = value
		self.nextNode = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.type = None
		# TODO: complete type checking


	def add_to_end(self, value=None):
		"""
		adds new node to list
		"""
		newNode = Node(value)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
			return

		# TODO: complete type checking
		self.tail.nextNode = newNode
		self.tail = self.tail.nextNode

	def count_elements(self):
		pass

	def find_by_value(self, v):
		pass

	def add_by_index(self, ind, v):
		# TODO: complete type checking
		pass

	def print(self):
		if self.head is None:
			return

		node = self.head
		while node is not None:
			print(node.value)
			node = node.nextNode

	def delete_last(self):
		self.tail = None

	def delete_by_value(self, value):
		if self.head is None:
			return
		if self.head.value == value:
			self.head = self.head.nextNode
			return

		currNode = self.head
		prevNode = None

		while currNode is not None:
			if currNode.value == value:
				prevNode.nextNode = currNode.nextNode
				break
			prevNode = currNode
			currNode = currNode.nextNode


class SortedLinkedList(LinkedList):
	def __init__(self):
		super().__init__()

	def add_to_end(self, value=None):
		pass



if __name__ == "__main__":
	mylist = LinkedList()
	mylist2 = LinkedList()
	mylist.add_to_end('5')
	mylist.add_to_end('hello')
	mylist.add_to_end('darkness')
	mylist.add_to_end('my old')
	mylist.add_to_end('friend')
	mylist.print()
	mylist.delete_by_value('5')
	mylist.print()

	myList2 = SortedLinkedList()




