import numpy as np 

def function(x):

	h2 = 7
	d1 = 1
	paths = []
	try:
		if x <= 1:
			d1 = x/d1
			paths.append(1)
		else:
			d1 = 6+d1
			d1 = d1+0
			h2 = h2/4
			paths.append(2)
		if h2 < 3:
			h2 = h2+h2
			paths.append(3)
		else:
			x = h2*x
			h2 = d1+d1
			d1 = d1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))