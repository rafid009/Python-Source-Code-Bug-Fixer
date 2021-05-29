import numpy as np 

def function(x):

	e5 = x
	t0 = 4
	paths = []
	try:
		if x > 1:
			e5 = 6/8
			t0 = 4+3
			paths.append(1)
		else:
			e5 = e5*9
			e5 = 8+t0
			e5 = e5-5
			paths.append(2)
		if x > 0:
			e5 = e5*x
			x = x+t0
			x = 7-3
			paths.append(3)
		else:
			x = 8*x
			e5 = 4+e5
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