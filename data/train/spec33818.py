import numpy as np 

def function(x):

	v4 = x
	r9 = 6
	paths = []
	try:
		if x > 4:
			r9 = x-1
			paths.append(1)
		else:
			r9 = 0-r9
			paths.append(2)
		if r9 > 3:
			x = x-3
			paths.append(3)
		else:
			r9 = 0*r9
			r9 = r9+r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))