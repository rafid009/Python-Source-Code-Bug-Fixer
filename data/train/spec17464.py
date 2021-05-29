import numpy as np 

def function(x):

	e5 = 2
	v9 = 3
	paths = []
	try:
		if v9 > 6:
			x = x+9
			x = v9*5
			x = 6*x
			paths.append(1)
		else:
			v9 = 2*v9
			e5 = e5*7
			e5 = v9*e5
			paths.append(2)
		if e5 >= 3:
			e5 = 1+e5
			e5 = 8-e5
			paths.append(3)
		else:
			v9 = v9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))