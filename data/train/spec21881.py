import numpy as np 

def function(x):

	e7 = 2
	r2 = 2
	paths = []
	try:
		if e7 < 1:
			r2 = r2*9
			x = 0-x
			paths.append(1)
		else:
			r2 = 9+r2
			e7 = 1-6
			paths.append(2)
		if e7 > 6:
			r2 = r2/r2
			x = 6/x
			x = x*9
			paths.append(3)
		else:
			r2 = e7+r2
			e7 = e7+0
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))