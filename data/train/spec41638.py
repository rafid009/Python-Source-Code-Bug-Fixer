import numpy as np 

def function(x):

	d7 = 0
	k0 = 2
	paths = []
	try:
		if d7 < 9:
			x = k0+x
			k0 = k0*6
			paths.append(1)
		else:
			d7 = 4*d7
			k0 = d7/k0
			paths.append(2)
		if k0 < 3:
			x = x-k0
			d7 = 4*d7
			d7 = d7+k0
			paths.append(3)
		else:
			d7 = d7-x
			d7 = k0-d7
			k0 = k0*2
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))