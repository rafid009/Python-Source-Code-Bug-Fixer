import numpy as np 

def function(x):

	p0 = 8
	d7 = 6
	paths = []
	try:
		if p0 >= 6:
			x = x+2
			d7 = 1-d7
			p0 = 6-p0
			paths.append(1)
		else:
			p0 = 9*d7
			x = 5*x
			paths.append(2)
		if d7 >= 7:
			x = p0*x
			p0 = 5-p0
			paths.append(3)
		else:
			x = x-1
			x = 6/9
			x = 3/d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))