import numpy as np 

def function(x):

	d8 = x
	p6 = x
	paths = []
	try:
		if d8 < 0:
			x = x-9
			p6 = 0*3
			d8 = d8*3
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if x >= 2:
			p6 = d8*7
			x = x/p6
			p6 = 4*p6
			paths.append(3)
		else:
			d8 = 4+d8
			x = d8/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))