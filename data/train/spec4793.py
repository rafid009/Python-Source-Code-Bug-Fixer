import numpy as np 

def function(x):

	x0 = x
	l2 = x
	paths = []
	try:
		if x0 < 4:
			x0 = x0-6
			paths.append(1)
		else:
			x0 = x0/x0
			x0 = 3/9
			l2 = 1/x0
			paths.append(2)
		if l2 >= 0:
			l2 = 4*8
			paths.append(3)
		else:
			l2 = l2/2
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))