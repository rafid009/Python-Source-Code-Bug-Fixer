import numpy as np 

def function(x):

	g4 = 6
	u0 = 2
	paths = []
	try:
		if x > 0:
			x = x-4
			g4 = 5+g4
			paths.append(1)
		else:
			u0 = u0-u0
			u0 = u0-8
			x = x/x
			paths.append(2)
		if u0 > 4:
			u0 = u0*6
			x = x-g4
			paths.append(3)
		else:
			u0 = u0-3
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))