import numpy as np 

def function(x):

	e3 = x
	p0 = x
	paths = []
	try:
		if p0 > 2:
			x = 0+p0
			paths.append(1)
		else:
			e3 = 6-e3
			paths.append(2)
		if p0 >= 5:
			x = 6-1
			x = 3/x
			paths.append(3)
		else:
			x = x/5
			e3 = 0-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))