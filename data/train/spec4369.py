import numpy as np 

def function(x):

	h5 = x
	p0 = x
	paths = []
	try:
		if p0 > 4:
			p0 = p0*4
			p0 = p0-p0
			paths.append(1)
		else:
			p0 = x+2
			h5 = x*h5
			h5 = 4*0
			paths.append(2)
		if h5 >= 2:
			x = 4-x
			x = 5-x
			paths.append(3)
		else:
			h5 = h5*3
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