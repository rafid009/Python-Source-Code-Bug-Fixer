import numpy as np 

def function(x):

	p1 = 0
	d0 = x
	paths = []
	try:
		if x <= 6:
			d0 = d0*2
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if p1 < 4:
			d0 = 9+d0
			paths.append(3)
		else:
			x = x/4
			d0 = d0*7
			d0 = d0*d0
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