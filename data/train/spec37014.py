import numpy as np 

def function(x):

	u0 = 5
	a3 = 2
	paths = []
	try:
		if a3 < 1:
			u0 = 0*u0
			paths.append(1)
		else:
			a3 = a3-9
			u0 = x*u0
			paths.append(2)
		if x <= 7:
			u0 = u0+9
			x = x-5
			paths.append(3)
		else:
			x = x-u0
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