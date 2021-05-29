import numpy as np 

def function(x):

	r9 = x
	x2 = x
	paths = []
	try:
		if x2 < 0:
			r9 = 2-r9
			x2 = x2-r9
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if x > 7:
			r9 = r9*8
			x = 2/x
			x2 = 9*x2
			paths.append(3)
		else:
			x2 = x2-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))