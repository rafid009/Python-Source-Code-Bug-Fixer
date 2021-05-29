import numpy as np 

def function(x):

	e0 = 7
	x1 = 8
	paths = []
	try:
		if e0 > 9:
			x = 1/x
			paths.append(1)
		else:
			e0 = x-7
			e0 = 7-8
			x1 = e0+0
			paths.append(2)
		if e0 < 3:
			x1 = e0+x1
			x = e0*8
			e0 = e0/x
			paths.append(3)
		else:
			x = x/x
			x = x1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))