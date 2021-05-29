import numpy as np 

def function(x):

	a3 = 4
	u2 = 0
	paths = []
	try:
		if a3 > 8:
			u2 = u2/6
			paths.append(1)
		else:
			u2 = 4*u2
			a3 = a3-3
			paths.append(2)
		if x > 3:
			a3 = 0+2
			x = 8+7
			paths.append(3)
		else:
			x = x+a3
			u2 = 5-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))