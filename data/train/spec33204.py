import numpy as np 

def function(x):

	r2 = x
	b1 = 7
	paths = []
	try:
		if r2 < 9:
			b1 = x-b1
			x = x*x
			x = 6-x
			paths.append(1)
		else:
			r2 = 1/r2
			x = x-3
			x = x*7
			paths.append(2)
		if r2 < 3:
			x = 2*x
			paths.append(3)
		else:
			b1 = 4+b1
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