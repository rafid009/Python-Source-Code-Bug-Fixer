import numpy as np 

def function(x):

	d2 = 8
	d4 = x
	x = x
	paths = []
	try:
		if x < 4:
			d4 = 2*x
			d2 = x-d4
			paths.append(1)
		else:
			d2 = d2+d2
			d4 = d4-3
			x = x/8
			paths.append(2)
		if x >= 3:
			d2 = 0/d2
			x = d4*3
			d2 = 8+6
			paths.append(3)
		else:
			d2 = d2+d2
			d4 = 8-2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d4 = d2**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))