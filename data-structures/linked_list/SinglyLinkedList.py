#!/usr/bin/python3

class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self._length = 0

	def __len__(self):
		print("length of llist :", self._length)
		return self._length

	def is_empty(self):
		return self._length == 0

	def insert(self, val):
		new_node = Node(val)

		if self.head is None:
			self.head = new_node
			return

	
		last = self.head
		while (last.next):
			last = last.next

		last.next = new_node

	def delete(self, val):
        current = self.head
        previous = None
        found = False
        while current and found is False:
        	if current.value == val
        		found = True
        	else:
        		previous = current
        		current = current.next
        if current is None:
        	raise ValueError
        if previous is None:
        	self.head = current.next
        else:
        	previous.next = current.next

	def search(self, val):
		current = self.head
		found = False
		while current and found is False:
			if current.value == val:
			    found = True
			else:
				current = current.next
		if current is None:
			raise ValueError
		return current

	def printList(self):
		current = self.head
		while(current):
			print(current.value)
			current = current.next


def ggg():
	#Some tests
	llist = SinglyLinkedList()
	llist.insert(1)
	llist.insert(2)
	llist.insert(3)
	llist.insert(4)
	llist.insert(5)
	llist.insert(6)
	llist.is_empty()
	llist.__len__()
	llist.printList()

if __name__ == '__main__':
	ggg()