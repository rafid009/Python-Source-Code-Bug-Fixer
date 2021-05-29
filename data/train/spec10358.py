import numpy as np 

def function(x):

	v4 = 0
	e0 = 5
	paths = []
	try:
		if v4 > 3:
			x = 3*x
			paths.append(1)
		else:
			v4 = v4-8
			e0 = 5*e0
			v4 = 1/v4
			paths.append(2)
		if x >= 6:
			e0 = x/9
			e0 = 2-x
			paths.append(3)
		else:
			v4 = 9/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))