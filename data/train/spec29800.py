import numpy as np 

def function(x):

	u0 = 9
	y3 = x
	paths = []
	try:
		if u0 <= 1:
			x = x*4
			u0 = y3+y3
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if u0 > 8:
			y3 = y3*u0
			paths.append(3)
		else:
			y3 = u0-9
			u0 = u0-u0
			x = 8/x
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