import numpy as np 

def function(x):

	e5 = x
	k2 = 0
	paths = []
	try:
		if x >= 9:
			k2 = 4-x
			paths.append(1)
		else:
			k2 = k2*3
			paths.append(2)
		if x >= 7:
			x = x+0
			paths.append(3)
		else:
			x = x*5
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