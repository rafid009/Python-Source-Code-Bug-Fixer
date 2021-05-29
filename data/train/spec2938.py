import numpy as np 

def function(x):

	d8 = x
	k3 = x
	paths = []
	try:
		if x > 1:
			x = k3-x
			d8 = 2-d8
			paths.append(1)
		else:
			d8 = 7+d8
			paths.append(2)
		if x > 8:
			x = x-2
			x = 2*d8
			paths.append(3)
		else:
			k3 = 0*x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))