import numpy as np 

def function(x):

	p0 = x
	a3 = x
	paths = []
	try:
		if a3 < 7:
			p0 = p0-5
			p0 = 1+6
			paths.append(1)
		else:
			x = a3*6
			paths.append(2)
		if p0 > 1:
			p0 = p0+4
			x = x+6
			x = p0-x
			paths.append(3)
		else:
			p0 = 3-p0
			p0 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))