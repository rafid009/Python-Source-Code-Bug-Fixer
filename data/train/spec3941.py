import numpy as np 

def function(x):

	e9 = x
	p0 = x
	x = 7
	paths = []
	try:
		if p0 > 0:
			x = p0*x
			p0 = 7/p0
			p0 = p0*x
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x >= 1:
			e9 = 2/5
			paths.append(3)
		else:
			p0 = 5+p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))