import numpy as np 

def function(x):

	p0 = x
	e0 = x
	paths = []
	try:
		if e0 >= 1:
			e0 = e0-p0
			e0 = e0+3
			paths.append(1)
		else:
			e0 = 8-9
			e0 = 3+8
			paths.append(2)
		if p0 <= 7:
			e0 = e0-0
			paths.append(3)
		else:
			x = e0+2
			e0 = 9*7
			x = x/4
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