import numpy as np 

def function(x):

	u0 = x
	x5 = 1
	paths = []
	try:
		if x5 <= 8:
			u0 = 1*u0
			u0 = u0*4
			x = 5-x
			paths.append(1)
		else:
			x5 = 7/u0
			u0 = u0*3
			x = x-3
			paths.append(2)
		if u0 <= 4:
			x = x+4
			paths.append(3)
		else:
			x = x*x5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))