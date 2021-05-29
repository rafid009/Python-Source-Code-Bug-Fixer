import numpy as np 

def function(x):

	a5 = 6
	k4 = x
	paths = []
	try:
		if x > 2:
			a5 = x+6
			k4 = k4-x
			x = 1*2
			paths.append(1)
		else:
			a5 = 6*8
			paths.append(2)
		if a5 <= 0:
			a5 = a5-9
			x = x-x
			paths.append(3)
		else:
			k4 = k4*5
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