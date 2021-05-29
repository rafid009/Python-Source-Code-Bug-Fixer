import numpy as np 

def function(x):

	l4 = x
	x5 = 4
	paths = []
	try:
		if x > 6:
			x = l4/x
			paths.append(1)
		else:
			x5 = 8+x5
			paths.append(2)
		if x5 < 3:
			x = x*8
			x5 = 2-x5
			x5 = x5/8
			paths.append(3)
		else:
			x = 3-x
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