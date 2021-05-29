import numpy as np 

def function(x):

	p0 = 9
	d6 = 7
	paths = []
	try:
		if x > 8:
			p0 = p0+5
			x = 7-x
			paths.append(1)
		else:
			x = x-d6
			paths.append(2)
		if p0 < 6:
			p0 = 8-p0
			paths.append(3)
		else:
			p0 = 9-p0
			d6 = d6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))