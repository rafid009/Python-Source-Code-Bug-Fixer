import numpy as np 

def function(x):

	u2 = 1
	a7 = x
	paths = []
	try:
		if a7 < 7:
			a7 = 5+a7
			a7 = 3*a7
			a7 = u2+a7
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if a7 < 8:
			u2 = 4-u2
			u2 = 0*u2
			paths.append(3)
		else:
			u2 = u2+1
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