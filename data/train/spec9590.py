import numpy as np 

def function(x):

	d0 = x
	v4 = x
	paths = []
	try:
		if x <= 8:
			v4 = v4+5
			v4 = v4+v4
			x = 2*x
			paths.append(1)
		else:
			v4 = v4/x
			paths.append(2)
		if d0 > 6:
			v4 = 9-v4
			paths.append(3)
		else:
			v4 = x*v4
			v4 = v4*x
			d0 = x-v4
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))