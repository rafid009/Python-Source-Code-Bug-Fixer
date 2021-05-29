import numpy as np 

def function(x):

	e6 = x
	u0 = x
	paths = []
	try:
		if x > 7:
			u0 = x-u0
			paths.append(1)
		else:
			u0 = e6/3
			u0 = x*u0
			x = u0/x
			paths.append(2)
		if u0 >= 4:
			e6 = u0+e6
			e6 = 7+e6
			x = 0-6
			paths.append(3)
		else:
			e6 = 7/4
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