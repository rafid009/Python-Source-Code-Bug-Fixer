import numpy as np 

def function(x):

	x8 = x
	n6 = 3
	paths = []
	try:
		if x8 >= 3:
			n6 = 3*n6
			paths.append(1)
		else:
			x = x+x8
			n6 = x8-n6
			paths.append(2)
		if n6 > 9:
			n6 = 4*n6
			paths.append(3)
		else:
			x8 = x8+x8
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))