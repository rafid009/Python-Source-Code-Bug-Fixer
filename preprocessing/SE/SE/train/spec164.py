import numpy as np 

def function(x):

	n0 = 6
	y4 = 8
	paths = []
	try:
		if x < 4:
			x = 4/x
			n0 = 8+8
			paths.append(1)
		else:
			n0 = n0/2
			paths.append(2)
		if x >= 9:
			y4 = 9*y4
			x = 2/y4
			paths.append(3)
		else:
			n0 = n0+x
			y4 = 5+y4
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))