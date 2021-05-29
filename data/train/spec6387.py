import numpy as np 

def function(x):

	d2 = x
	d1 = x
	paths = []
	try:
		if x >= 6:
			d2 = d2+d1
			d1 = d1+d2
			d1 = 8-d1
			paths.append(1)
		else:
			d1 = 6-d1
			d1 = 4*d1
			paths.append(2)
		if x <= 3:
			x = 2+d2
			x = 3+d1
			paths.append(3)
		else:
			x = x+4
			d2 = d1-d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d1 = d2**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))