import numpy as np 

def function(x):

	p0 = 5
	e2 = 7
	paths = []
	try:
		if e2 > 2:
			p0 = p0-4
			paths.append(1)
		else:
			e2 = e2+3
			e2 = e2-5
			paths.append(2)
		if x >= 6:
			x = x*3
			x = 8*x
			paths.append(3)
		else:
			x = 4*x
			e2 = 3+e2
			p0 = p0+3
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