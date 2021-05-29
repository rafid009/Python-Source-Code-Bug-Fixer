import numpy as np 

def function(x):

	e0 = 4
	o3 = 1
	paths = []
	try:
		if x >= 4:
			e0 = e0-1
			x = x/9
			e0 = 0/5
			paths.append(1)
		else:
			e0 = o3/e0
			x = 4*x
			paths.append(2)
		if e0 < 9:
			x = x+x
			paths.append(3)
		else:
			x = x-3
			x = 5+x
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