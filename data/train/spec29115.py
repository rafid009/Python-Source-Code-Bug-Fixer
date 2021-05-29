import numpy as np 

def function(x):

	d2 = 6
	p0 = x
	x = 7
	paths = []
	try:
		if p0 >= 9:
			p0 = p0/p0
			paths.append(1)
		else:
			d2 = 0+8
			x = 2+0
			p0 = 3*p0
			paths.append(2)
		if x >= 1:
			d2 = 5-d2
			paths.append(3)
		else:
			x = d2-3
			d2 = x-7
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))