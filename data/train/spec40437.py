import numpy as np 

def function(x):

	n8 = 7
	d5 = x
	paths = []
	try:
		if x >= 2:
			x = x+8
			paths.append(1)
		else:
			n8 = n8-n8
			d5 = d5*d5
			n8 = n8+n8
			paths.append(2)
		if n8 > 6:
			d5 = 6/3
			n8 = 8-n8
			paths.append(3)
		else:
			d5 = d5-4
			d5 = 1*8
			x = x-d5
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