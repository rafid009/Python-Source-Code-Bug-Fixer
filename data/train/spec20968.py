import numpy as np 

def function(x):

	v2 = 5
	d4 = 2
	paths = []
	try:
		if d4 < 1:
			d4 = d4+3
			paths.append(1)
		else:
			d4 = d4+x
			d4 = 7/d4
			paths.append(2)
		if d4 >= 4:
			x = 9/x
			paths.append(3)
		else:
			x = 6*7
			d4 = v2-x
			d4 = 9*d4
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