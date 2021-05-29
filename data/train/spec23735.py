import numpy as np 

def function(x):

	x7 = x
	d2 = x
	paths = []
	try:
		if d2 >= 7:
			x7 = x*x7
			paths.append(1)
		else:
			x = 0*8
			x7 = x7-x7
			paths.append(2)
		if d2 < 4:
			d2 = x7-d2
			paths.append(3)
		else:
			x7 = x7/d2
			d2 = 2/d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x7 = d2**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))