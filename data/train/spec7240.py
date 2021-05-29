import numpy as np 

def function(x):

	n0 = x
	y6 = 8
	paths = []
	try:
		if x > 6:
			n0 = n0+3
			n0 = n0/3
			paths.append(1)
		else:
			n0 = 7*n0
			paths.append(2)
		if n0 <= 5:
			n0 = n0/n0
			n0 = x/4
			y6 = y6/y6
			paths.append(3)
		else:
			x = x/4
			y6 = y6*3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))