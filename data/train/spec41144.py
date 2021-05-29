import numpy as np 

def function(x):

	a8 = 3
	u2 = 4
	paths = []
	try:
		if x >= 8:
			u2 = 8+u2
			u2 = u2-6
			u2 = u2+u2
			paths.append(1)
		else:
			u2 = a8+6
			u2 = 4/u2
			u2 = u2*u2
			paths.append(2)
		if x > 6:
			a8 = a8/6
			x = x*a8
			u2 = a8*a8
			paths.append(3)
		else:
			a8 = 3*a8
			a8 = a8+x
			a8 = 5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))