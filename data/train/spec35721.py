import numpy as np 

def function(x):

	d8 = 0
	z4 = 7
	paths = []
	try:
		if z4 > 9:
			d8 = d8-3
			paths.append(1)
		else:
			z4 = x+5
			paths.append(2)
		if z4 > 8:
			d8 = d8*1
			x = 8+x
			d8 = d8/9
			paths.append(3)
		else:
			d8 = 1-d8
			x = x*d8
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))