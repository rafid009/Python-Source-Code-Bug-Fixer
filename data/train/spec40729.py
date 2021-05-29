import numpy as np 

def function(x):

	h6 = 6
	p0 = x
	paths = []
	try:
		if h6 >= 1:
			h6 = 4/h6
			h6 = 7*p0
			p0 = p0+6
			paths.append(1)
		else:
			h6 = h6-0
			h6 = h6+p0
			p0 = p0*2
			paths.append(2)
		if h6 > 6:
			x = x+1
			h6 = 6*2
			h6 = h6/h6
			paths.append(3)
		else:
			h6 = h6/2
			p0 = x*p0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))