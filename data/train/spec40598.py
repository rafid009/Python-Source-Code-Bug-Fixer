import numpy as np 

def function(x):

	l4 = x
	d1 = 8
	paths = []
	try:
		if x <= 8:
			x = 0/x
			d1 = d1/8
			x = x+l4
			paths.append(1)
		else:
			x = 9*x
			d1 = d1/x
			d1 = 1*d1
			paths.append(2)
		if x >= 3:
			d1 = d1/d1
			d1 = 9+d1
			x = x/x
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		d1 = l4**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))