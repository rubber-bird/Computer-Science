#!/usr/bin/python3
from SinglyLinkedList import Node
from SinglyLinkedList import SinglyLinkedList

def main():
	#Some tests
	llist = SinglyLinkedList
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
	main()