import numpy as np 

def function(x):

	e0 = 3
	v9 = 4
	paths = []
	try:
		if e0 > 1:
			x = 4-x
			v9 = v9*v9
			paths.append(1)
		else:
			v9 = v9-v9
			paths.append(2)
		if x < 8:
			e0 = 6+e0
			paths.append(3)
		else:
			e0 = e0*9
			e0 = e0+9
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