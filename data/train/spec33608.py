import numpy as np 

def function(x):

	n3 = 7
	y0 = x
	paths = []
	try:
		if n3 <= 0:
			y0 = 0+y0
			n3 = 0/n3
			n3 = n3+7
			paths.append(1)
		else:
			n3 = 2+7
			x = 1+y0
			paths.append(2)
		if x >= 9:
			y0 = 9/y0
			x = 4+7
			n3 = y0-n3
			paths.append(3)
		else:
			y0 = 6-y0
			n3 = 2*n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))