import numpy as np 

def function(x):

	e8 = 3
	p0 = 9
	paths = []
	try:
		if e8 > 2:
			e8 = e8+e8
			paths.append(1)
		else:
			e8 = e8*x
			p0 = e8/p0
			paths.append(2)
		if e8 > 5:
			p0 = p0/p0
			e8 = e8+x
			paths.append(3)
		else:
			x = x*6
			e8 = 4+e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))