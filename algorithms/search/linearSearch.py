#!/usr/bin/python3

def search(arr, n, x):
	for i in range(0, n):
		if arr[i] == x:
			return i
	return -1
