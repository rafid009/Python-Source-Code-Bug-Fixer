import numpy as np 

def function(x):

	w9 = 5
	e0 = x
	paths = []
	try:
		if x < 9:
			w9 = 6/w9
			x = 8+x
			x = 3+x
			paths.append(1)
		else:
			x = 9/x
			w9 = 9+w9
			w9 = 9-6
			paths.append(2)
		if w9 < 9:
			e0 = 8/e0
			e0 = e0*5
			e0 = 3/9
			paths.append(3)
		else:
			w9 = 4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))