import numpy as np 

def function(x):

	u0 = 4
	a4 = x
	paths = []
	try:
		if a4 <= 3:
			u0 = u0+u0
			u0 = 1/7
			paths.append(1)
		else:
			a4 = x*a4
			a4 = a4-5
			paths.append(2)
		if x < 3:
			a4 = a4-x
			x = 0-x
			paths.append(3)
		else:
			x = u0-x
			x = 0+9
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