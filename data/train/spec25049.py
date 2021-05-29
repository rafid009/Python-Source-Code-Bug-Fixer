import numpy as np 

def function(x):

	d4 = x
	r3 = x
	paths = []
	try:
		if d4 < 2:
			x = x/9
			d4 = 0-d4
			paths.append(1)
		else:
			x = x/3
			d4 = d4/x
			paths.append(2)
		if r3 > 6:
			r3 = 0*r3
			paths.append(3)
		else:
			x = x/r3
			x = 5/d4
			r3 = 2*r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))