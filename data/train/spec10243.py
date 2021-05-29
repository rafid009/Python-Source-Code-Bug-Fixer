import numpy as np 

def function(x):

	n6 = x
	x8 = x
	paths = []
	try:
		if x >= 5:
			x8 = x8*n6
			n6 = n6+5
			x8 = x8+8
			paths.append(1)
		else:
			x8 = x8*n6
			paths.append(2)
		if x < 9:
			x8 = 2*n6
			paths.append(3)
		else:
			x8 = x8-4
			n6 = n6*4
			n6 = n6/n6
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		n6 = x8**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))