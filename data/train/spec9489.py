import numpy as np 

def function(x):

	d6 = 6
	h4 = 3
	x = x
	paths = []
	try:
		if h4 <= 8:
			d6 = d6*x
			x = x*h4
			d6 = d6*d6
			paths.append(1)
		else:
			x = 2*d6
			h4 = h4*2
			x = 1+x
			paths.append(2)
		if h4 > 4:
			d6 = 5/x
			h4 = h4/4
			paths.append(3)
		else:
			h4 = h4-x
			h4 = h4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))