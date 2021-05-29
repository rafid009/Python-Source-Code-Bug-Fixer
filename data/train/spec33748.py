import numpy as np 

def function(x):

	u3 = x
	e0 = 1
	paths = []
	try:
		if u3 < 8:
			e0 = 0*u3
			e0 = 5+e0
			paths.append(1)
		else:
			e0 = 5*e0
			e0 = 0/e0
			paths.append(2)
		if x > 5:
			x = 0-9
			u3 = e0-x
			e0 = e0-e0
			paths.append(3)
		else:
			e0 = e0/1
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