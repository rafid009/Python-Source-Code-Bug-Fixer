import numpy as np 

def function(x):

	x6 = x
	n0 = x
	paths = []
	try:
		if n0 > 5:
			x = x-3
			x6 = 7-x6
			paths.append(1)
		else:
			n0 = 0-x6
			n0 = n0+n0
			x = 6-x
			paths.append(2)
		if x6 > 2:
			x6 = x6*n0
			x6 = x6*8
			x6 = x6*2
			paths.append(3)
		else:
			x6 = x+3
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))