import numpy as np 

def function(x):

	p0 = x
	h3 = x
	paths = []
	try:
		if h3 >= 6:
			p0 = x-h3
			p0 = 3*0
			paths.append(1)
		else:
			p0 = p0*2
			paths.append(2)
		if h3 >= 4:
			h3 = h3/h3
			p0 = h3-5
			paths.append(3)
		else:
			h3 = h3-4
			p0 = h3*4
			p0 = 4*p0
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