import numpy as np 

def function(x):

	n4 = x
	x8 = 3
	paths = []
	try:
		if n4 >= 1:
			x = x/6
			x8 = x8+8
			x8 = n4-x8
			paths.append(1)
		else:
			x8 = x8-x
			paths.append(2)
		if x >= 3:
			n4 = x8*3
			paths.append(3)
		else:
			x8 = 4-5
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x8 = n4**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))