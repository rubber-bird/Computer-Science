
#! /usr/bin/python3

def bubbleSort(array):
  for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
  return array