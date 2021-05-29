import numpy as np 

def function(x):

	n6 = 8
	x8 = x
	paths = []
	try:
		if n6 > 3:
			x = x-5
			x8 = 9-x8
			n6 = 6+n6
			paths.append(1)
		else:
			x8 = x8*x
			paths.append(2)
		if x < 6:
			x8 = x8-x8
			paths.append(3)
		else:
			n6 = 6+x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))