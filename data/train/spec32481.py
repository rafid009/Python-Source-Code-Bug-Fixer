import numpy as np 

def function(x):

	y3 = 2
	n0 = x
	paths = []
	try:
		if n0 >= 5:
			y3 = 4+n0
			x = x+8
			x = 4*x
			paths.append(1)
		else:
			n0 = 5-n0
			paths.append(2)
		if y3 > 1:
			x = x*7
			n0 = y3+y3
			y3 = 3-n0
			paths.append(3)
		else:
			n0 = 3+n0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))