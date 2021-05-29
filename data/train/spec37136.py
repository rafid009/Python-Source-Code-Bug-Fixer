import numpy as np 

def function(x):

	d7 = x
	d4 = x
	paths = []
	try:
		if d4 < 7:
			x = 6/d4
			paths.append(1)
		else:
			d7 = x*x
			paths.append(2)
		if d4 > 1:
			x = d4*x
			d7 = d7*9
			d7 = 0+d7
			paths.append(3)
		else:
			d4 = x-d4
			x = d7/x
			d7 = d7-9
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))