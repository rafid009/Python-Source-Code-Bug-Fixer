import numpy as np 

def function(x):

	d7 = 1
	n7 = 7
	paths = []
	try:
		if d7 <= 2:
			d7 = n7*d7
			d7 = d7-d7
			d7 = d7-d7
			paths.append(1)
		else:
			x = d7*3
			paths.append(2)
		if d7 <= 0:
			n7 = 8*n7
			d7 = 0-2
			paths.append(3)
		else:
			x = n7-1
			n7 = 4-7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		n7 = d7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))