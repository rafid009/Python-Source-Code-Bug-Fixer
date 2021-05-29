import numpy as np 

def function(x):

	n6 = x
	d8 = 4
	paths = []
	try:
		if x >= 4:
			x = x*6
			d8 = 5/d8
			paths.append(1)
		else:
			d8 = d8+0
			d8 = 6/5
			paths.append(2)
		if d8 <= 5:
			n6 = n6+4
			n6 = 0-d8
			n6 = 6+n6
			paths.append(3)
		else:
			d8 = 8-d8
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