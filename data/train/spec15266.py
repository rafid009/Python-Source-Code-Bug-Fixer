import numpy as np 

def function(x):

	k9 = 1
	d0 = x
	paths = []
	try:
		if d0 >= 1:
			k9 = k9+8
			k9 = k9-3
			k9 = 8/k9
			paths.append(1)
		else:
			x = k9*d0
			d0 = x-7
			paths.append(2)
		if x > 4:
			k9 = k9+9
			paths.append(3)
		else:
			k9 = k9+3
			k9 = 7-5
			d0 = k9-d0
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