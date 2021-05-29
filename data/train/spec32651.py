import numpy as np 

def function(x):

	h3 = 8
	d2 = 9
	paths = []
	try:
		if h3 >= 6:
			d2 = x*d2
			x = 3*x
			d2 = d2+x
			paths.append(1)
		else:
			d2 = 1-d2
			paths.append(2)
		if x > 9:
			d2 = 2+d2
			paths.append(3)
		else:
			h3 = 9/h3
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))