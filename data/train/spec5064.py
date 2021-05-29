import numpy as np 

def function(x):

	x3 = x
	l8 = 0
	paths = []
	try:
		if x > 5:
			x3 = x3*3
			x3 = x3+4
			paths.append(1)
		else:
			l8 = 0-8
			l8 = x-l8
			paths.append(2)
		if x > 0:
			x3 = l8-1
			x = x/7
			l8 = l8-7
			paths.append(3)
		else:
			x = 2+x
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