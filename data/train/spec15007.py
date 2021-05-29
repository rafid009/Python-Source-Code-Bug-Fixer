import numpy as np 

def function(x):

	k0 = 2
	d1 = 1
	paths = []
	try:
		if k0 < 8:
			k0 = 4+k0
			k0 = 4*k0
			paths.append(1)
		else:
			d1 = 0+d1
			d1 = d1-4
			paths.append(2)
		if x <= 4:
			x = 6+x
			d1 = d1/4
			k0 = k0*1
			paths.append(3)
		else:
			x = x+6
			d1 = 4/k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))