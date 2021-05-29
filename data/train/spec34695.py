import numpy as np 

def function(x):

	n8 = 0
	x0 = x
	paths = []
	try:
		if x0 <= 4:
			x = x-x0
			paths.append(1)
		else:
			x = n8*6
			n8 = n8-2
			paths.append(2)
		if x0 > 9:
			n8 = n8-2
			paths.append(3)
		else:
			x0 = x0-6
			x0 = 9+6
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))