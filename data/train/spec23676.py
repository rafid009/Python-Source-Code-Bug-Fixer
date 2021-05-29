import numpy as np 

def function(x):

	d4 = 7
	d5 = 8
	paths = []
	try:
		if d4 >= 2:
			d4 = d4+d4
			x = x*d4
			paths.append(1)
		else:
			d5 = 8+7
			d4 = d4+6
			paths.append(2)
		if x >= 3:
			d5 = d5+8
			x = x-x
			d5 = d4+d5
			paths.append(3)
		else:
			x = 1*x
			d5 = d4*d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))