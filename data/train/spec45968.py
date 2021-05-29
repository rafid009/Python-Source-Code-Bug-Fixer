import numpy as np 

def function(x):

	k9 = x
	d0 = 6
	paths = []
	try:
		if k9 > 4:
			x = k9*x
			d0 = d0*3
			k9 = x-6
			paths.append(1)
		else:
			d0 = x-3
			d0 = x*d0
			paths.append(2)
		if x > 1:
			x = x*2
			x = x*k9
			paths.append(3)
		else:
			x = 6*k9
			d0 = x*8
			d0 = 7-d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))