import numpy as np 

def function(x):

	r2 = x
	n6 = 2
	paths = []
	try:
		if n6 < 4:
			n6 = n6/9
			x = n6-x
			paths.append(1)
		else:
			r2 = 0*r2
			paths.append(2)
		if r2 <= 5:
			r2 = 3/r2
			paths.append(3)
		else:
			x = 1*r2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))