from .stack import Stack

class Queue:
	# Two stack implementation
	# FIFO (First in first out)

	def __init__(self):
		self.master = Stack()
		self.slave = Stack()

	def length(self):
		return self.master.size + self.slave.size

	def is_empty(self):
		return self.master.is_empty() and self.slave.is_empty()

	def enqueue(self, x):
		self.master.push(x)

	def dequeue(self):
		if self.length() == 0:
			raise Exception('Queue is empty!')
		if self.slave.is_empty():
			while not self.master.is_empty():
				self.slave.push(self.master.pop())
		return self.slave.pop()

	def peek(self):
		if self.length() == 0:
			return None
		if self.slave.is_empty():
			while not self.master.is_empty():
				self.slave.push(self.master.pop())
		return self.slave.peek()
