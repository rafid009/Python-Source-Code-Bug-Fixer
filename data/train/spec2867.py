import numpy as np 

def function(x):

	d1 = 4
	d2 = 9
	paths = []
	try:
		if d1 < 2:
			d2 = x*d2
			d1 = 8-d1
			d1 = d1/d1
			paths.append(1)
		else:
			d2 = d2+6
			x = 4/x
			paths.append(2)
		if d2 < 1:
			d1 = 2/d1
			x = x*x
			paths.append(3)
		else:
			d2 = d2-8
			x = x*8
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