import numpy as np 

def function(x):

	r4 = 2
	d4 = x
	paths = []
	try:
		if r4 <= 0:
			d4 = d4/r4
			x = d4*x
			d4 = 1-9
			paths.append(1)
		else:
			d4 = 6/d4
			paths.append(2)
		if x < 7:
			r4 = r4-2
			paths.append(3)
		else:
			r4 = r4+4
			r4 = 6/r4
			x = x/9
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