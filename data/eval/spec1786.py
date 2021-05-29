import numpy as np 

def function(x):

	d2 = x
	k2 = x
	paths = []
	try:
		if k2 >= 6:
			x = 4/x
			x = d2/3
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if x <= 1:
			x = 2/x
			k2 = k2/k2
			paths.append(3)
		else:
			d2 = d2*x
			d2 = 4*d2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		d2 = k2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))