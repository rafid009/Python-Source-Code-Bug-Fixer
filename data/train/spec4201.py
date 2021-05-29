import numpy as np 

def function(x):

	y5 = x
	u0 = 1
	paths = []
	try:
		if x < 1:
			u0 = u0+6
			u0 = u0-8
			x = x+9
			paths.append(1)
		else:
			x = 6-x
			x = 3*u0
			paths.append(2)
		if u0 >= 9:
			u0 = 1+8
			u0 = 7+u0
			paths.append(3)
		else:
			y5 = u0-y5
			x = 2/x
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