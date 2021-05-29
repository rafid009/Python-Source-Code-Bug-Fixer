import numpy as np 

def function(x):

	u0 = x
	y3 = x
	paths = []
	try:
		if y3 < 0:
			u0 = u0*6
			u0 = u0/8
			x = x+x
			paths.append(1)
		else:
			u0 = u0-7
			y3 = 2*x
			y3 = y3/u0
			paths.append(2)
		if u0 < 6:
			u0 = u0+u0
			paths.append(3)
		else:
			y3 = 0*y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))