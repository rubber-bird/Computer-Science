#!/usr/bin/env python3

class Stack:
	def __init__(self):
		self.stack = []
		self.size = 0

	def empty(self):
		return self.size == 0

	def top(self):
		return self.stack[self.size-1] 

	def push(self, val):
		self.stack.append(val)
		self.size += 1

	def pop(self):
		self.stack.pop()
		self.size -= 1



	