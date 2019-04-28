class LinkedListNode:
	# Standard singly linkedlist node

	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		return str(self.val)

	def print_forward(self):
		# No need for extra space
		# Space complexity: O(1)
		cur = self
		while cur is not None:
			print(str(cur.val) + " -> ", end='')
			cur = cur.next
		print("None")

	def print_backward(self):
		# Space complexity: O(n) because of recursion
		if self.next is None:
			print(self.val)
			return
		self.next.print_backward()
		print(self.val)

	def add_to_front(self, node):
		node.next = self
		return node

	def length(self):
		length = 0
		cur = self
		while cur is not None:
			length += 1
			cur = cur.next
		return length


class LinkedList:
	# Wrapper for LinkedListNode

	def __init__(self):
		print("Not friendly for recursion. Be careful!")
		self.head = None

	def __str__(self):
		cur = self.head
		val_list = []
		while cur is not None:
			val_list.append(str(cur.val))
			cur = cur.next
		return 'None' if len(val_list) == 0 else ' -> '.join(val_list) + ' -> None'

	def add_to_front(self, node):
		node.next = self.head
		self.head = node