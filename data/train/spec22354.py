import numpy as np 

def function(x):

	v1 = x
	e4 = 5
	paths = []
	try:
		if x >= 4:
			e4 = e4-v1
			x = x/v1
			paths.append(1)
		else:
			v1 = e4/7
			paths.append(2)
		if e4 < 2:
			e4 = e4/4
			paths.append(3)
		else:
			x = 9+x
			e4 = e4+x
			v1 = 9*v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))