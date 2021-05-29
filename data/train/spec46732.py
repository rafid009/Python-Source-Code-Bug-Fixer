import numpy as np 

def function(x):

	u0 = 2
	a8 = x
	paths = []
	try:
		if a8 > 0:
			a8 = a8/2
			paths.append(1)
		else:
			x = a8-u0
			paths.append(2)
		if a8 > 2:
			a8 = x+x
			u0 = a8/u0
			u0 = u0/6
			paths.append(3)
		else:
			u0 = a8-u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		u0 = u0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))