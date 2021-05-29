import numpy as np 

def function(x):

	y9 = 1
	d5 = x
	paths = []
	try:
		if d5 < 1:
			d5 = x*d5
			d5 = d5/8
			x = 5-x
			paths.append(1)
		else:
			x = 1+y9
			y9 = 0-0
			paths.append(2)
		if y9 > 8:
			d5 = 7+d5
			d5 = d5/8
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))