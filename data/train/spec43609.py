import numpy as np 

def function(x):

	a3 = 3
	p0 = 2
	paths = []
	try:
		if x >= 7:
			p0 = p0-x
			paths.append(1)
		else:
			a3 = a3*5
			paths.append(2)
		if x > 3:
			x = x+x
			x = a3+4
			x = x-8
			paths.append(3)
		else:
			a3 = p0*a3
			p0 = p0*a3
			p0 = 3/p0
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