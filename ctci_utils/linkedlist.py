class LinkedListNode:
	# Standard singly linkedlist node

	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		return str(self.val)


class LinkedList:
	# Wrapper for LinkedListNode

	def __init__(self):
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