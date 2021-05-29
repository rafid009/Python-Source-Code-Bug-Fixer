import numpy as np 

def function(x):

	e0 = x
	p0 = x
	paths = []
	try:
		if x <= 9:
			x = x-4
			x = 6*x
			e0 = e0-0
			paths.append(1)
		else:
			p0 = p0+3
			paths.append(2)
		if p0 <= 2:
			p0 = 2+p0
			paths.append(3)
		else:
			p0 = e0+3
			e0 = x-p0
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))