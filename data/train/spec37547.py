import numpy as np 

def function(x):

	q8 = x
	i5 = 0
	x = 7
	paths = []
	try:
		if i5 < 1:
			x = 8*4
			x = 8-1
			x = q8*4
			paths.append(1)
		else:
			q8 = i5*8
			x = 0-i5
			paths.append(2)
		if x < 1:
			i5 = x+i5
			paths.append(3)
		else:
			q8 = 8*q8
			i5 = q8+6
			x = 6-i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		q8 = i5**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))