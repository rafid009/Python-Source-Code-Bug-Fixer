import numpy as np 

def function(x):

	n0 = 1
	y1 = 4
	paths = []
	try:
		if x >= 9:
			x = y1*3
			n0 = 7*n0
			y1 = 9*3
			paths.append(1)
		else:
			n0 = n0/8
			n0 = 0-8
			paths.append(2)
		if n0 <= 6:
			y1 = y1+y1
			x = x*x
			paths.append(3)
		else:
			x = x-3
			x = x-y1
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		y1 = n0**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))