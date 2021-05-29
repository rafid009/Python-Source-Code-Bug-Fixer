import numpy as np 

def function(x):

	e4 = 2
	r6 = x
	paths = []
	try:
		if x <= 1:
			x = 5/x
			paths.append(1)
		else:
			r6 = e4+x
			r6 = x+6
			paths.append(2)
		if x <= 8:
			r6 = r6-r6
			paths.append(3)
		else:
			x = x-r6
			e4 = 7/e4
			e4 = r6*4
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