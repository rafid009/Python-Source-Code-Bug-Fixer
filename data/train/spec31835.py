import numpy as np 

def function(x):

	x4 = 4
	l1 = x
	paths = []
	try:
		if x > 2:
			x4 = 3+1
			x = 6*x
			x = x-3
			paths.append(1)
		else:
			l1 = l1-3
			l1 = 5-9
			paths.append(2)
		if x >= 4:
			x = 0*3
			x4 = 2*x4
			l1 = 4+3
			paths.append(3)
		else:
			x = 8-x
			x4 = l1/x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))