import numpy as np 

def function(x):

	d9 = x
	paths = []
	try:
		if x > 8:
			d9 = d9/2
			x = x-2
			x = 2*x
			paths.append(1)
		else:
			d9 = 1+d9
			paths.append(2)
		if x > 0:
			d9 = 0+d9
			x = x-d9
			d9 = 8+8
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))