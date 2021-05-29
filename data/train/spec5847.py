import numpy as np 

def function(x):

	d0 = x
	k2 = 7
	paths = []
	try:
		if d0 > 8:
			x = x-4
			k2 = k2*7
			paths.append(1)
		else:
			k2 = k2/2
			d0 = d0/3
			paths.append(2)
		if d0 < 8:
			d0 = 0-k2
			x = k2+1
			paths.append(3)
		else:
			k2 = k2+5
			d0 = 6*d0
			d0 = 7+4
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))