import numpy as np 

def function(x):

	v9 = 4
	e8 = 7
	paths = []
	try:
		if e8 < 3:
			x = e8/v9
			e8 = e8+e8
			x = 9+x
			paths.append(1)
		else:
			e8 = e8+e8
			e8 = 2/4
			paths.append(2)
		if x > 3:
			x = x*x
			paths.append(3)
		else:
			x = x*v9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))