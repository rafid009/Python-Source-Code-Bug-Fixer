import numpy as np 

def function(x):

	d5 = x
	n0 = x
	x = 0
	paths = []
	try:
		if n0 < 3:
			d5 = d5-1
			paths.append(1)
		else:
			x = 6+6
			paths.append(2)
		if n0 <= 6:
			d5 = x+d5
			paths.append(3)
		else:
			n0 = x-4
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		d5 = n0**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))