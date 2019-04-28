from .linkedlist import LinkedListNode

class Stack:
	# LIFO (Last in first out)

	def __init__(self):
		self.top = None
		self.size = 0

	def push(self, x):
		node = LinkedListNode(x)
		node.next = self.top
		self.top = node
		self.size += 1

	def pop(self):
		if self.top is None:
			raise Exception('Stack is empty!')
		ret = self.top.val
		self.top = self.top.next
		self.size -= 1
		return ret

	def print_stack(self):
		if self.top is None:
			print("None")
		else:
			self.top.print_forward()