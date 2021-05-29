import numpy as np 

def function(x):

	e2 = 9
	o3 = x
	paths = []
	try:
		if e2 < 6:
			e2 = e2*6
			o3 = x+o3
			e2 = 9-e2
			paths.append(1)
		else:
			x = x*e2
			paths.append(2)
		if o3 <= 8:
			o3 = x*e2
			e2 = o3/4
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))