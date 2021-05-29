import numpy as np 

def function(x):

	r8 = 0
	e0 = 1
	paths = []
	try:
		if e0 < 9:
			r8 = r8*x
			r8 = r8/e0
			paths.append(1)
		else:
			x = x/r8
			e0 = 9-x
			paths.append(2)
		if x > 1:
			r8 = x/8
			paths.append(3)
		else:
			r8 = r8*5
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