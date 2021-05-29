import numpy as np 

def function(x):

	y9 = 4
	d7 = 5
	paths = []
	try:
		if y9 < 0:
			x = d7+x
			d7 = 8*x
			d7 = 8/x
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x < 8:
			d7 = 7-d7
			paths.append(3)
		else:
			d7 = 1*d7
			y9 = 7/4
			d7 = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))